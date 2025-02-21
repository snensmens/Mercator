# Contributing
Thanks for your interest in contributing to Mercator!

## Building
You can build Mercator using Flatpak Builder:
1. Install Flatpak Builder if you have not already done so
    ```
    flatpak install flathub org.flatpak.Builder
    ```

2. Clone and enter the Repository:
    ```
   git clone https://github.com/snensmens/Mercator.git
   
   cd Mercator
   ```

3. Build and install the application
    ```
   flatpak run org.flatpak.Builder --force-clean --user --install build-dir com.github.snensmens.Mercator.json
   ```
   
4. Run the application
    ```
   flatpak run com.github.snensmens.Mercator
   ```
   
## Add translations
If you want to contribute translation to the app

### Add a new language
1. Check if your language is already added for translations under `po/LINGUAS`
   
   if not, add the country code of your country (2-digit ISO 3166-1) to the file. (eg. `es` for Spain)

2. Create a new po file for your language
   ```
   // replace {locale} and {country-code} according to your language
   msginit -i po/com.github.snensmens.Mercator.pot --locale={locale} -o po/{country-code}.po
   
   // example for creating a po file for spanish (spain) language:
   msginit -i po/com.github.snensmens.Mercator.pot --locale=es_ES -o po/es.po
   ```
   
### Update
```
msgmerge --update po/{language}.po po/com.github.snensmens.Mercator.pot
```