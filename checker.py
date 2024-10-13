import ssl
import certifi
import urllib.request

def check_ssl_certificates():
    # Get the path to the latest CA certificates
    ca_certs_path = certifi.where()

    # Set the SSL context to use the CA certificates
    ssl_context = ssl.create_default_context(cafile=ca_certs_path)

    try:
        # Test the SSL context by opening a secure connection to a known site
        with urllib.request.urlopen("https://calcuis.us", context=ssl_context) as response:
            print("SSL certificates are up-to-date and SSL context is functional.")
            print(f"Response code: {response.status}")
    except Exception as e:
        print(f"Error: SSL certificates or context might not be configured properly. Details: {e}")

check_ssl_certificates()
