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
  <a href="https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Log Ingestor and Query Interface</h3>

  <p align="center">
    Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters.
    <br />
    <a href="https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot">View Demo</a>
    ·
    <a href="https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Screenshot from 2023-11-19 22-52-37](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/17c0fe45-b35a-4cef-a42e-1cb4e26d4085)





<!-- GETTING STARTED -->
## Getting Started

 Firstly, setting up this into your local system going to be easy with some catch.
 1. Download zip and extract all files --> in folder static, create a  folder FILE  because this folder was empty and got hidden while uploading it.
 2. Install python3.8 or above.
 3. Use requirement.txt to install all required package for this project.
 4. Generate a OPENAI_API_KEY from its OpenAI website and copy-paste into a text file as it will be useful ahead.
 5. There are some defauft name which are as follow:
         1. log.db - for database
         2. log    - table name where all log data is stored.
 6. Sample folder has file format in which we can upload json and csv files.
         

### Prerequisites

Instruction must be executed before running the project.
* requirements.txt
  ```sh
  pip install -r requirements. txt  
  ```

### Installation

1. Get a free OPENAI_API_Key at [OPENAI API](https://openai.com/blog/openai-api)
2. Clone the repo
   ```sh
   git clone https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot.git
   ```
3. Create a .env file and paste OPENAI_API_KEY.
   ```sh
   OPENAI_API_Key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
   ```
4. RUN app.py 
   ```sh
   python3 app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

We can upload json or csv file using uploading box.
![Screenshot from 2023-11-19 23-30-21](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/0ddaaa42-7e5f-4f8f-8688-2defa0e88469)



Here we selected our sample file data.csv 
![Screenshot from 2023-11-19 23-31-00](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/92892b46-2960-488d-99f1-9146b2e2e87e)



 Uploaded it and it will be save in static/FILE/data.csv  (*AT starting created FILE folder)

![Screenshot from 2023-11-19 23-31-28](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/d5dc1502-edd4-4be8-9289-793933b07b6e)



Using full-text search for logs having message="failed to connect to db"

![Screenshot from 2023-11-19 23-39-35](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/e761709a-2f68-4782-911a-6aaffb7f1ebb)




Output from embedchain bot.

![Screenshot from 2023-11-19 23-34-34](https://github.com/dyte-submissions/november-2023-hiring-HrithikShah/assets/42888428/074dffa6-dd87-4892-804c-a08c8663d2e0)







<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

Log Ingestor:

- [ ] Develop a mechanism to ingest logs in the provided format.
- [ ] Ensure scalability to handle high volumes of logs efficiently.
- [ ] itigate potential bottlenecks such as I/O operations, database write speeds, etc.
- [ ] Make sure that the logs are ingested via an HTTP server, which runs on port 3000 by default.

Query Interface:

- [ ] Offer a user interface (Web UI or CLI) for full-text search across logs.
- [ ] Aim for efficient and quick search results.



See the [open issues](https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [Hrithik Shah](https://www.linkedin.com/in/hrithikhshah107/) - hrithikhshah10137@gmail.com

Project Link: [https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot](https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* www.python.com
* www.embedchain.ai
* www.flask.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HrithikShah/log-ingestor-System-with-AI-Query-bot.svg?style=for-the-badge
[contributors-url]: https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HrithikShah/log-ingestor-System-with-AI-Query-bot.svg?style=for-the-badge
[forks-url]: https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/network/members
[stars-shield]: https://img.shields.io/github/stars/HrithikShah/log-ingestor-System-with-AI-Query-bot.svg?style=for-the-badge
[stars-url]: https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/HrithikShah/log-ingestor-System-with-AI-Query-bot.svg?style=for-the-badge
[issues-url]: https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/issues
[license-shield]: https://img.shields.io/github/license/HrithikShah/log-ingestor-System-with-AI-Query-bot.svg?style=for-the-badge
[license-url]: https://github.com/HrithikShah/log-ingestor-System-with-AI-Query-bot/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/hrithikhshah107
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
