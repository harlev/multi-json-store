<h1 align="center">Welcome to multi-json-store 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/harlev/multi-json-store/blob/master/LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/harlev" target="_blank">
    <img alt="Twitter: harlev" src="https://img.shields.io/twitter/follow/harlev.svg?style=social" />
  </a>
</p>

> Store JSON in multiple stores simultaniously 

The goal of this library is to enable redundency when storing data to a JSON store.  
There are four built in JSON Storage services
* https://jsonbox.io/
* https://jsonbin.io/
* https://jsonstorage.net/
* https://getpantry.cloud/

A simple sequence
```
js = JsonStore()
js.create('{"a": 1}')
js.update('{"a": 3}')
js.read()
```
will result, as expected, in a sequence of create/update/read to all four storage services

Run the simple [tests](https://github.com/harlev/multi-json-store/blob/master/tests/test_store.py) to see it in action

## Setup
Popoulate `keys.py` with the keys from the different services.

## Extending
Other services which implement a REST API for JSON storage could be added.  
Extend `AbstractJsonStorage` and implement all the `@abstractmethod`.  
Follow the examples in the existing implementations. The designs attempts to make the code needed as minimal as possible.

## Author

👤 **Ron Harlev**

* Twitter: [@harlev](https://twitter.com/harlev)
* Github: [@harlev](https://github.com/harlev)
* LinkedIn: [@harlev](https://linkedin.com/in/harlev)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/harlev/multi-json-store/issues). 

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2020 [Ron Harlev](https://github.com/harlev).<br />
This project is [MIT](https://github.com/harlev/multi-json-store/blob/master/LICENSE) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
