from api.extract_competitions import extract_competitions
from api.extract_complexes import extract_complexes
from api.extract_rankings import extract_rankings

from transform.transform_competitions import (
    transform_competitions
)
from transform.transform_complexes import (
    transform_complexes
)
from transform.transform_rankings import (
    transform_rankings
)


def main() -> None:
    """Run the complete API extraction and transformation pipeline."""

    print("Starting data extraction...")

    extract_competitions()
    extract_complexes()
    extract_rankings()

    print("Starting data transformation...")

    transform_competitions()
    transform_complexes()
    transform_rankings()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()