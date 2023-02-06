import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import create_tag, create_user
from views import create_entry
from views import delete_entry, delete_entry_tag_with_entryid
<<<<<<< HEAD
from views import get_all_moods
from views import get_single_entry, get_all_entries, get_all_entry_tags
from views import update_user
=======
from views import get_all_moods, get_single_mood
from views import get_single_entry, get_all_entries, search_journal_entries
from views import update_user, update_entry
>>>>>>> main

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """
    def parse_url(self, path):
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split('/')
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
            elif resource == "entries":
                if id is not None and id < len(get_all_entries()):
                    self._set_headers(200)
                    response = get_single_entry(id)
                elif id is None:
                    self._set_headers(200)
                    response = get_all_entries()
                else:
                    self._set_headers(404)
<<<<<<< HEAD
            if resource == "entry_tags":
                self._set_headers(200)
                response = get_all_entry_tags()
            self.wfile.write(json.dumps(response).encode())
=======
        else:
            (resource) = parsed
            if resource == "entries_search":
                if "q" in parsed[1]:
                    search_term = parsed[1]["q"][0]
                    self._set_headers(200)
                    response = search_journal_entries(search_term)
                else:
                    self._set_headers(400)
                    response = {"error": "missing search term"}

        self.wfile.write(json.dumps(response).encode())
>>>>>>> main

    def do_POST(self):
        """ posts new data to the database """
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)

        new_data = None

        if resource == "entries":
            self._set_headers(201)
            new_data = create_entry(post_body)
        elif resource == "tags":
            self._set_headers(201)
            new_data = create_tag(post_body)

        elif resource == "users":
            self._set_headers(201)
            new_data = create_user(post_body)
        elif resource is not 'entries' or 'tags':
            self._set_headers(404)

            self.wfile.write(json.dumps(new_data).encode())

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
        ##
        #

    # Delete a single animal from the list
        if resource == "users":
            update_user(id, post_body)
        if resource == "entries":
            update_entry(id, post_body)

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
