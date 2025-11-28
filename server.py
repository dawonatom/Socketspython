import socket
import threading

def receive_messages(client_socket):
    """Función que se ejecuta en un hilo separado para recibir mensajes."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\nCliente: {message}")
                print("Tú: ", end="", flush=True) # Mantiene el prompt visualmente
            else:
                # Conexión cerrada
                break
        except:
            break
    print("\nEl cliente se ha desconectado.")
    client_socket.close()

def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Servidor iniciado en {host}:{port}. Esperando conexión...")

        client_socket, addr = server_socket.accept()
        print(f"Conexión establecida con {addr}")

        # Iniciar hilo para recibir mensajes
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True # El hilo muere si el programa principal termina
        receive_thread.start()

        # Bucle principal para enviar mensajes
        while True:
            msg = input("Tú: ")
            if msg.lower() == 'salir':
                client_socket.close()
                break
            client_socket.send(msg.encode('utf-8'))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        server_socket.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    start_server()