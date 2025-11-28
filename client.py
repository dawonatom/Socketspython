import socket
import threading

def receive_messages(client_socket):
    """Función que se ejecuta en un hilo separado para recibir mensajes."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\nServidor: {message}")
                print("Tú: ", end="", flush=True)
            else:
                break
        except:
            break
    print("\nDesconectado del servidor.")
    client_socket.close()

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Conectado al servidor en {host}:{port}")
        print("Escribe 'salir' para terminar.")

        # Iniciar hilo para recibir mensajes
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        # Bucle principal para enviar mensajes
        while True:
            msg = input("Tú: ")
            if msg.lower() == 'salir':
                client_socket.close()
                break
            client_socket.send(msg.encode('utf-8'))

    except ConnectionRefusedError:
        print("No se pudo conectar. Asegúrate de que el servidor esté encendido.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Cliente cerrado.")

if __name__ == "__main__":
    start_client()