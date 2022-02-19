# Smart Projector Screen

This project involves making a dumb projector screen with a RF remote a smart one by triggering button presses on the remote via a Raspberry PI.

<center>

![](assets/setup.jpg)

_don't let your kids near this_

</center>

## FAQ

### Couldn't you have just used a 433Mhz RF transmitter?

Yes.

## Setup

- Make sure you have python3
- `pip install -r requirements.txt`

## Usage

- Start the server by running `./server.py`
- The API is now availble on `http://0.0.0.0:8080`

| Path    | Method | Query Parameters | Description                                                                                                                                                             |
| ------- | ------ | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/up`   | `POST` | `None`           | Causes the screen to completely roll up.                                                                                                                                |
| `/down` | `POST` | `timeout=5`      | Causese the screen to roll down, use the `timeout` parameter to issue a stop command after a specific time, useful for controlling how far down the screen should roll. |
| `/stop` | `POST` | `None`           | Sends a stop signal, will halt whatever the operation that was in progress.                                                                                             |
