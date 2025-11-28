# Chat Bidireccional con Python Sockets 🐍

Este proyecto implementa un chat simple cliente-servidor utilizando Sockets y Threading en Python. Permite comunicación bidireccional simultánea (full-duplex), donde ambos usuarios pueden enviar y recibir mensajes al mismo tiempo sin bloquear la terminal.

## Requisitos

* Python 3.x instalado.

## Estructura

* `server.py`: Script que inicia el servidor y espera conexiones.
* `client.py`: Script que se conecta al servidor.

## Instrucciones de Uso

1.  **Iniciar el Servidor:**
    Abre una terminal y ejecuta:
    ```bash
    python server.py
    ```

2.  **Iniciar el Cliente:**
    Abre **otra** terminal y ejecuta:
    ```bash
    python client.py
    ```

3.  **Chatear:**
    Escribe mensajes en cualquiera de las consolas. Para salir, escribe `salir`.

## Conceptos Aplicados
* **Sockets (TCP/IP):** Para la conexión de red.
* **Threading:** Para manejar la recepción de mensajes en segundo plano sin bloquear el input del usuario.
