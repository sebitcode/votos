<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Documentacion del Proyecto</h3>

  <p align="center">
    Esta documentacion servira como guia durante la revisión del proyecto
    <br />
    <a href="https://github.com/cookiecutter/cookiecutter-django"><strong>Cookiecutter »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenido</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#steps">Steps</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    Steps
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

En este proyecto nos centramos en realizar un esquema basico para registrar los votantes de un evento, Sin embargo si se encuentran fallas en el mismo es debido a su reciente realización en futaras versiones todos los errores reportados seran corregidos por nuestro equipo, Gracias.



### Built With

* [![Python][Python.py]][Python-url]
* [![Django REST framework][Django REST framework.py]][Django REST framework-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Este es un ejemplo de como inicializar 
el proyecto de forma local.
Para obtener una copia y correrla
sigue los siguientes pasos.

### Prerequisites

Estas son las cosas que vas a necesitar para ejecutar el proyecto desde una mac y como instalarlas.

### Installation

1. Get Docker at [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
1.5 Get Brew at [https://mac.install.guide/homebrew/3.html](https://mac.install.guide/homebrew/3.html)
2. Get Docker Compose Plugin at [https://formulae.brew.sh/formula/docker-compose#default](https://formulae.brew.sh/formula/docker-compose#default)
3. Download the repo as a ZIP
4. Build containers before get up the project
   ```sh
   docker-compose -f local.yml build
   ```
5. Migrate models
   ```sh
   docker-compose -f local.yml run --rm django python manage.py migrate
   ```
6. Set up the base data
   ```sh
   docker-compose -f local.yml run --rm django python manage.py base-data
   ```
7. Run the project
   ```sh
   docker-compose -f local.yml up
   ```
4. Set the POSTMAN collection `Votos.postman_collection.json` is already in project folder

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Todos los endpoints estan protegidos
por un token que se debe pedir cada
determinado tiempo los niveles de
los permisos de los token estan segmentados segun el tipo de usuario que los pida.

_Para obtener el token debe consultarlo con un usuario y contraseña, puede usar las de prueba si ejecuto el command base-data `votos/locations/management/commands/utils/leaders.json` ó `votos/locations/management/commands/utils/administrators.json`_

_Una vez obtenido el token debe poner lo en las variables de entorno_

_En las variables de entorno tambien debe poner el host ej. `localhost:8000`_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] API Rest usando JSON
- [ ] debe utilizarse el API de Georreferenciación de Google
- [x] Servicio de Login (usuario y contraseña)
    - [x] POST (usuario y contraseña)
    - [x] RESPONSE (TOKEN)
- [x] Validar la existencia del Token en los servicios
- [x] Cada servicio, debe tener un CRUD
- [x] Un servicio para obtener la cantidad total de votantes
    - [x] Por lider
    - [x] En el sistema
    - [x] Por municipio
    - [x] Por mesa

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Steps

- Modelado
- Serializers
- Views
- Enrutamientos
- Validaciones
- Pruebas

_Todo se hizo siendo lo mas fiel al framework por ende se asegura el uso de buenas practicas_

_Tambien se implento la estragia de JWT para las autorizaciones por Token y el manejo de sesiones_

_La base de datos es de tipo relacional (PostgreSQL)_

_Se utilizo la estragia de los contenedores para separar funcionalidades pero como tal solo es necesario un 2 contenedores siendo estos Django y PostGres_

_Se hicieron varias pruebas antes de dar por finalizada la API Rest_


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->
## Contact

Sebastian Herrera Granada - sebitcode@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Django Docs](https://docs.djangoproject.com/en/4.0/)
* [Python Best Practice](https://www.codingdojo.com/blog/python-best-practices)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Pydanny](https://github.com/pydanny)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Python-url]: https://www.python.org/
[Python.py]: https://img.shields.io/badge/python.py-000000?style=for-the-badge&logo=Python&logoColor=white
[Django REST framework-url]: https://www.django-rest-framework.org/
[Django REST framework.js]: https://img.shields.io/badge/Django.py-green?style=for-the-badge&logo=Django&logoColor=white
