# Power Apps

Dwie aplikacje canvas zbudowane na tej samej bazie filmowej i tym samym pomyśle: *nie zastanawiaj się, po prostu wylosuj*.

| Aplikacja | Co robi | Kod |
|---|---|---|
| **Kartoteka** | Powerappsowa siostra streamlitowej apki z tego repo. Losuje film ze 130 polskich klasyków, pokazuje kartę z plakatem, zbiera oceny i recenzje na liście SharePoint. | [`kartoteka/`](kartoteka/) |
| **Koło Fortuny** | Koło losuje kategorię, z kategorii leci pytanie „A czy B”. Osoby do odpytania wybiera się z listy zespołu, ta sama nie wypada trzy razy pod rząd. | [`kolo-fortuny/`](kolo-fortuny/) |

## Jak używać tych plików

Power Apps Studio nie importuje całych aplikacji z plików tekstowych, ale **przyjmuje pojedyncze kontrolki i całe ekrany przez schowek**. Dlatego kod leży tu w dwóch formatach:

- **`App.OnStart.fx`** — treść właściwości `OnStart` obiektu `App`. Otwórz `App` w drzewie kontrolek, wybierz `OnStart` i wklej całość do paska formuły.
- **`screens/*.pa.yaml`** — jeden plik na ekran, w formacie *Source Code* (Power Apps YAML). Otwórz pusty ekran, kliknij w tło i wciśnij **Ctrl+V**.

### Trzy pułapki, które kosztowały najwięcej czasu

1. **W pasku formuły nie wpisuje się `=`.** W YAML-u każda właściwość ma prefiks `=`, bo tak wymaga format pliku. Wklejenie tego znaku do Studia daje `expected operator`.
2. **W YAML-u nie może być spacji po dwukropku wewnątrz rekordu.** `{Imie: x}` w jednoliniowej właściwości parser czyta jako zagnieżdżoną mapę i wywala `YamlInvalidSyntax`. Piszemy `{Imie:x}` albo przenosimy formułę do bloku `|-`.
3. **Właściwość `HtmlText` musi być jedną linią** wewnątrz bloku `|-`. Rozbicie jej na wiele linii nie zgłasza błędu — po prostu kontrolka renderuje pustkę.

### Wersje kontrolek

Pliki YAML odwołują się do konkretnych wersji: `HtmlViewer@2.1.0`, `Classic/Button@2.2.0`, `Classic/TextInput@2.3.2`, `Classic/ComboBox@2.4.0`, `Classic/DropDown@2.3.1`, `Classic/Icon@2.5.0`, `Label@2.5.1`, `Image@2.2.3`, `Timer@2.1.0`, `Audio@2.3.1`, `Rating@2.1.0`, `Gallery@2.15.0`. Galeria wymaga jeszcze wiersza `Variant` — `Vertical` albo `VariableHeight`. Nieznana wersja lub wariant kończy się błędem `PA2109` przy wklejaniu.

### Czego HtmlViewer nie renderuje

Kontrolka przepuszcza `div`, `border-radius`, `box-shadow`, `conic-gradient`, `transform`, `position:absolute`, `flex`, a nawet `@keyframes` w bloku `<style>`. **Wycina za to `<svg>`** — cała zawartość znika bez śladu i bez błędu. Dlatego koło fortuny jest zbudowane z gradientów CSS, a nie z wektorów, a fajerwerki po wylosowaniu to osobna kontrolka `Image` z SVG zakodowanym jako `data:` URI (tam działa, bo to obrazek, nie kod strony).
