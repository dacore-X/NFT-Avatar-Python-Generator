import os
import random
import glob
import json

from PIL import Image
from typing import List, Tuple
from hashlib import sha1


def randomize_passable(chance: int) -> bool:
    random_int: int = random.randint(0, 100)
    if random_int <= chance:
        return True
    return False


def gen_hash(attributes: List[dict]):
    x = ''
    for attribute in attributes:
        for _, value in attribute.items():
            x += value
    return sha1(x.encode('utf-8')).hexdigest()


def randomize_rarity(rarity_paths: List[str]) -> str:
    weights: List[int] = []
    rarities: List[str] = []
    for rarity_path in rarity_paths:
        rarity_name = rarity_path.split('\\')[-1]
        rarity_chance = CHANCES_RARITY[rarity_name]
        rarities.append(rarity_name)
        weights.append(rarity_chance)

    return random.choices(
        rarities,
        weights=weights,
        k=1
    )[0]


def create_metadata(image_hash: str, attributes: List[dict]):
    metadata: dict = {
        "name": image_hash,
        "description": "Generated Funny Mummy Troll",
        "image": "IPFS URL",
        "attributes": attributes
    }
    return json.dumps(metadata)


CHANCES_RARITY: dict = {
    'epic': 10,  # Probability of Epic trait = 10%
    'rare': 30,  # Probability of Rare trait = 30%
    'common': 60  # Probability of Common trait = 60%
}

CHANCES_PASSABLE: dict = {
    'background': 0,  # Probability of Passing trait = 0%
    'body': 0,  # Probability of Passing trait = 0%
    'outerwear': 0,  # Probability of Passing trait = 0%
    'eyes': 0,  # Probability of Passing trait = 0%
    'eyebrows': 20,  # Probability of Passing trait = 20%
    'hat': 50,  # Probability of Passing trait = 50%
    'accessories': 80  # Probability of Passing trait = 80%
}


def gen_avatar(counter: int):
    attributes: List[dict] = []  # Used traits
    path: str = os.path.abspath(os.getcwd())
    traits_path: str = path + '\\input'
    traits_folders: List[str] = glob.glob(traits_path + '\\*', recursive=False)

    image: Image = Image.new('RGB', SIZE_OF_TRAITS)

    for trait_folder_path in traits_folders:
        trait_type: str = trait_folder_path.split('\\')[-1].split('-')[-1]
        if CHANCES_PASSABLE[trait_type] and randomize_passable(CHANCES_PASSABLE[trait_type]):
            continue

        rarity_folders: List[str] = glob.glob(trait_folder_path + '\\*', recursive=False)
        chosen_rarity: str = randomize_rarity(rarity_folders)
        traits_in_folder: List[str] = glob.glob(trait_folder_path + f'\\{chosen_rarity}' + '\\*', recursive=False)
        chosen_trait: str = random.choice(traits_in_folder)
        chosen_trait_name: str = chosen_trait.split('\\')[-1].split('.')[0]

        attribute: dict = {
            "trait_type": f"{trait_type.capitalize()}",
            "trait_rarity": f"{chosen_rarity.capitalize()}",
            "value": f"{chosen_trait_name.capitalize()}"
        }
        attributes.append(attribute)

        trait: Image = Image.open(chosen_trait)
        image.paste(trait, (0, 0), trait)

    image_hash: str = gen_hash(attributes)
    image.save(f'output/result_{counter}.png')

    metadata = create_metadata(image_hash, attributes)
    print(metadata)
    return metadata


def main():
    HASH_LIST: List[str] = []
    for i in range(AMOUNT_TO_GENERATE):
        hashed_avatar = json.loads(gen_avatar(i))['name']
        while hashed_avatar in HASH_LIST:
            hashed_avatar = gen_avatar(i)
        HASH_LIST.append(hashed_avatar)


if __name__ == '__main__':
    AMOUNT_TO_GENERATE: int = 15  # Amount of images to generate
    SIZE_OF_TRAITS: Tuple[int, int] = (1000, 1000)
    main()

