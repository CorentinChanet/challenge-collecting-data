
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
<!--[![MIT License][license-shield]][license-url] -->
<!--[![Issues][issues-shield]][issues-url] -->

  <h2 align="center">Collecting data challenge</h2>
  <p align="center">
    <a href="https://github.com/CorentinChanet/challenge-collecting-data">
    <img src="https://github.com/CorentinChanet/challenge-collecting-data/blob/readme/logo_Bouman_3.31.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">
    Web scraping group project as a part of Data&AI training at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a>
    <br />

  </h3>

</p>

<h2> Description </h2>

Our program will scrape a real estate website ([Immoweb](https://www.immoweb.be/en)) for data about houses and apartments
in Belgium. Once the information is fetched it will be cleaned and stored in a CSV file.


<h2> Installation </h2>

1. Clone the repo
2. Install the required libraries
3. Change the values 
4. Run main.py

```
pip3 install -r requirements.txt
```

<h2> Starting and running</h2>

After starting, our program will ask you to select a web driver for Selenium, based on your system, and provide a name for an output file. You may also specify how many search pages you want to scrape thus limiting the number of real estate you need to have information about.

Then a Selenium web driver would grab a list of links via the Immoweb search page starting from the most newer real estate. After collecting individual links (about 30 per page), our program will make an http request to each fetching the data with BeautifulSoup.

The flow of our program is designed in a such way that it will not crash or interrupt if the link or information on it would be incomplete or corrupted in any way. Fetching information is done with multi-threading to be on par with Selenium scraping. We also use a random timeout to not be noticed or banned from the site.

<h2> Output </h2>

Data would be outputted in 2 files: raw_data.csv and clean_data.csv.

Our program will give these fields about each property: locality, type of property (house or apartment, bungalow, chalet, mansion...), price, type of sale (exclusion or life sale), number of rooms, area, kitchen type, garden, terrace, and swimming pool availability as well as some additional properties.

Values would be stored as strings and numbers (including True and False indicating 1 and 0 correspondingly). 
Missing or impropriate values would be converting to None in a data frame resulting in am an empty cell in a CSV output file.

<h2> Contributors </h2>
<a href="https://github.com/hakanErgin"><strong>Hakan</strong></a>  
<a href="https://github.com/CorentinChanet"><strong>Corentin</strong></a>  
<a href="https://github.com/nicesoul"><strong>Vadym</strong></a>  


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License.

<!-- CONTACT -->
## Contact
Please, contact any of contributor via GitHub

## Acknowledgements
Thank you, Bouman! :)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CorentinChanet/challenge-collecting-data.svg?style=for-the-badge
[contributors-url]: https://github.com/CorentinChanet/challenge-collecting-data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CorentinChanet/challenge-collecting-data.svg?style=for-the-badge
[forks-url]: https://github.com/CorentinChanet/challenge-collecting-data/network/members
[stars-shield]: https://img.shields.io/github/stars/CorentinChanet/challenge-collecting-data.svg?style=for-the-badge
[stars-url]: https://github.com/CorentinChanet/challenge-collecting-data/stargazers
[issues-shield]: https://img.shields.io/github/issues/CorentinChanet/challenge-collecting-data.svg?style=for-the-badge
[issues-url]: https://github.com/CorentinChanet/challenge-collecting-data/issues
[license-shield]: https://img.shields.io/github/license/CorentinChanet/challenge-collecting-data.svg?style=for-the-badge
[license-url]: https://github.com/CorentinChanet/challenge-collecting-data/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
