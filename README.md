# ⚡**NFT Avatar Python Generator**⚡
![NFT examples](https://user-images.githubusercontent.com/86720231/175123204-85d4be94-49f6-414d-9666-a1ef060c20a9.png)

## **About**
Simple implementation of a generator with drawn traits.
You can generate your own NFT collection, however, you need to use a specific file location structure, which will be shown later.

## **Getting started**
1. Install requirements
```sh
pip install -r requirements.txt
```
2. Structure of input traits
- You need to use this structure of input folder with Your traits.
```sh
input
  ├───1-background
  │   ├───common
  │   ├───epic
  │   └───rare
  ├───2-body
  │   ├───common
  │   └───epic
  ├───3-outerwear
  │   ├───common
  │   ├───epic
  │   └───rare
  ├───4-eyes
  │   ├───common
  │   ├───epic
  │   └───rare
  ├───5-eyebrows
  │   └───common
  ├───6-hat
  │   ├───common
  │   ├───epic
  │   └───rare
  └───7-accessories
      ├───common
      └───epic
```
- You can change the names of the folders with traits (1-background, 2-body, ...) and rarity (common, rare, epic) then it is necessary to change some values in the code. The probability is also variable
**For Rarity:**
```sh
CHANCES_RARITY: dict = {
    'epic': 10,  # Probability of Epic trait = 10%
    'rare': 30,  # Probability of Rare trait = 30%
    'common': 60  # Probability of Common trait = 60%
}
```
**For Traits:**
```sh
CHANCES_PASSABLE: dict = {
    'background': 0,  # Probability of Passing trait = 0%
    'body': 0,  # Probability of Passing trait = 0%
    'outerwear': 0,  # Probability of Passing trait = 0%
    'eyes': 0,  # Probability of Passing trait = 0%
    'eyebrows': 20,  # Probability of Passing trait = 20%
    'hat': 50,  # Probability of Passing trait = 50%
    'accessories': 80  # Probability of Passing trait = 80%
}
```
3. Run [main.py] to generate collection

The settings for generation can also be configured.
```sh
AMOUNT_TO_GENERATE: int = 15  # Amount of images to generate
SIZE_OF_TRAITS: Tuple[int, int] = (1000, 1000)  # The size of Trait
```

4. Your collection is in the **output folder**

Metadata is closely built on the [principle of OpenSea](https://docs.opensea.io/docs/metadata-standards).

5. Create GIF from output data

Run [gif_create.py] to create GIF from avatars in **output folder**

**EXAMPLE:**

![result](https://user-images.githubusercontent.com/86720231/175123154-c8ff1b94-b011-4b6c-a6c2-70afce0cd2ab.gif)

