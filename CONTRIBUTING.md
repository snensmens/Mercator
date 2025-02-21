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