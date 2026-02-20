import random, json

from app.models.world import *

REGION_NAMES = [
                "RG-CENTRAL-1", "RG-NORTH-1", "RG-SOUTH-1", "RG-EAST-1", "RG-WEST-1",
                "RG-CENTRAL-2", "RG-NORTH-2", "RG-SOUTH-2", "RG-EAST-2", "RG-WEST-2"
            ]

# This does not need to take input because the world is generated.
# Eventually I will add seed functionality which then may require input.
# make name changeable
def create_new_world() -> WorldOutResponse:
    """
    Generates a new world with regions and trade links based on those regions

    Future:
    - Add input for name and seed
    - Once Responses are cached check if seed exists in cache and return day
      version of the world.
    :return WorldOutResponse:
    """
    regions = create_regions()
    trade_links = create_tradelinks(regions)

    world_out_response = WorldOutResponse(
        world_id="Joseph-" + regions[0].region_id+str(regions[0].population),
        trade_links=trade_links,
        regions=regions,
        name = "Joseph"
    )
    return world_out_response

def create_regions() -> List[RegionConfig]:
    """
    Generates a list of regions to be assigned to a World.

    There are 10 potential regions with 2 per cardinal direction and 2 central
    Regions represent the pieces on the board that is the world. They are were
    events come to life through ticking
    :return List[RegionConfig]:
    """
    list_of_regions = []
    used_region_id_indexes = set()

    num_of_regions = random.randint(5, 10)

    # Generate between 5 and 10 Regions
    for _ in range(num_of_regions):
        name_index = random.randint(0, len(REGION_NAMES)-1)

        # Generates a new random index for the chance of generating a used name_index
        while name_index in used_region_id_indexes:
            name_index = random.randint(0, len(REGION_NAMES)-1)

        region = RegionConfig(
            region_id=REGION_NAMES[name_index],
            name = "Test_Name",
            population = random.randint(1000000,100000000),
            employment_rate = round(random.random(),3),
            food_supply = round(random.random(),3),
            energy_supply = round(random.random(),3),
            price_index = round(random.random(),3),
            stability = round(random.random(),3),
        )

        used_region_id_indexes.add(name_index)
        list_of_regions.append(region)

    return list_of_regions

def create_tradelinks(list_of_regions: List[RegionConfig]) -> List[TradeLinkConfig]:
    '''
    Generates a list of trade links. Each region has at least one trade link
    but not every region is guaranteed to have an import trade link.

    This may change to be each region receives at least one trade link. Then
    the more outgoing trade links (exports) a region different affects may
    take place from events.
    :param list_of_regions:
    :return List[TradeLinkConfig]:
    '''
    list_of_tradelinks = []
    for index_of_from_region in range(len(list_of_regions)):

        index_of_to_region = random.randint(0, len(list_of_regions)-1)
        while index_of_to_region == index_of_from_region:
            index_of_to_region = random.randint(0, len(list_of_regions)-1)

        trade_to_region = list_of_regions[index_of_to_region]
        trade_from_region = list_of_regions[index_of_from_region]

        tradelink = TradeLinkConfig(
            from_region_id=trade_from_region.region_id,
            to_region_id=trade_to_region.region_id,
            capacity=random.randint(1,10),
            efficiency= round(random.random(),3),
            resources = ["food","energy"]
        )

        list_of_tradelinks.append(tradelink)

    return list_of_tradelinks

# def region_metrics(list_of_regions: List[RegionConfig]) -> None:
#     largest_population = 0
#     largest_name = ""
#     used_region_ids = []
#     most_unstable = 2
#     most_unstable_name = ""
#
#     for region in list_of_regions:
#         if region.population > largest_population:
#             largest_name = region.region_id
#             largest_population = region.population
#         if region.stability < most_unstable:
#             most_unstable = region.stability
#             most_unstable_name = region.region_id
#
#
#         used_region_ids.append(region.region_id)
#
#     print("--- Metrics ---")
#     print("Number of Regions: ", len(list_of_regions))
#     print("Used Region Ids: ", used_region_ids)
#     print("Largest Population [",largest_name,"]:", largest_population)
#     print("Most Unstable [",most_unstable_name,"]:", most_unstable)
#
# def tradelink_metrics(list_of_tradelinks: List[TradeLinkConfig]) -> None:
#     print("--- Metrics ---")
#     print("Number of Regions: ", len(list_of_tradelinks))
#     for tradelink in list_of_tradelinks:
#         print(tradelink)

# if __name__ == "__main__":
#     world_regions = create_regions()
#     world_tradelinks = create_tradelinks(world_regions)
#
#     print(create_world())