import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import delete_entry, delete_entry_tag_with_entryid
from views import get_all_moods
from views import get_single_entry, get_all_entries
from views import update_user

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')  # ['', 'animals', 1]
        resource = path_params[1]
        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)
        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def do_GET(self):
        """Handles GET requests to the server """
        parsed = self.parse_url(self.path)

        if '?' not in self.path:
            (resource, id) = parsed

            if resource == "moods":
                if id is not None and id < len(get_all_moods()):
                    self._set_headers(200)
                    response = get_single_mood(id)
                elif id is None:
                    self._set_headers(200)
                    response = get_all_moods()
            if resource == "entries":
                if id is not None and id < len(get_all_entries()):
                    self._set_headers(200)
                    response = get_single_entry(id)
                elif id is None:
                    self._set_headers(200)
                    response = get_all_entries()
                else:
                    self._set_headers(404)

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """docstring"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)
        response = []
        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        self.wfile.write(json.dumps(response).encode())

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        """docstring"""
    # Set a 204 response code
        self._set_headers(204)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

    # Delete a single animal from the list
        if resource == "entries":
            delete_entry(id)
            delete_entry_tag_with_entryid(id)

    # Encode the new animal and send in response
        self.wfile.write("".encode())

    def do_PUT(self):
        """docstring"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

    # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # success = False

    # Delete a single animal from the list
        if resource == "users":
            update_user(id, post_body)

    # Encode the new animal and send in response
        self.wfile.write("".encode())
# point of this application.


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
