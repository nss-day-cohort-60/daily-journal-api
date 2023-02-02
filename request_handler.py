import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_all_species, get_all_snakes, get_snakes_by_species
from views import get_single_species, get_single_snake
from views import get_all_owners, get_single_owner

#create functions
from views import create_tag

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

            if resource == "species":
                if id is not None and id < len(get_all_species()):
                    self._set_headers(200)
                    response = get_single_species(id)
                elif id is None:
                    self._set_headers(200)
                    response = get_all_species()
                else:
                    self._set_headers(404)

            elif resource == "snakes":
                if id is not None and id < len(get_all_snakes()):
                    snake = get_single_snake(id)
                    if snake['species']['name'] == "Aonyx cinerea":
                        self._set_headers(405)
                    else:
                        self._set_headers(200)
                        response = snake
                elif id is None:
                    self._set_headers(200)
                    response = get_all_snakes()
                else:
                    self._set_headers(404)

            elif resource == "owners":
                if id is not None:
                    self._set_headers(200)
                    response = get_single_owner(id)
                elif id is None:
                    self._set_headers(200)
                    response = get_all_owners()
                else:
                    self._set_headers(404)
            else:
                self._set_headers(404)
        else:
            self._set_headers(200)
            (resource, query) = parsed

            if query.get('species_id') and resource == 'snakes':
                response = get_snakes_by_species(query['species_id'][0])

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """docstring"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        new_snake = None
        new_owner = None
        new_species = None
        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "snakes":
            new_snake = create_snake(post_body)

        if resource == "owners":
            new_owner = create_owner(post_body)

        if resource == "tags":
            new_species = create_tag(post_body)

        if resource != 'snakes' or 'owners' or 'species':
            self._set_headers(404)

        # Encode the new animal and send in response
            self.wfile.write(json.dumps(new_snake).encode())

            self.wfile.write(json.dumps(new_owner).encode())

            self.wfile.write(json.dumps(new_species).encode())

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
        if resource == "orders":
            delete_order(id)

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

    # Delete a single animal from the list
        if resource == "metals":
            update_metal(id, post_body)

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
