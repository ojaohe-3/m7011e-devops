import json
import random
from typing import List, Set, Dict
from dataclasses import dataclass
import faker

# Initialize Faker for generating realistic data
fake = faker.Faker()

# Constants for random generation
PRODUCT_CATEGORIES = {
    "ELECTRONICS": ["Smartphones", "Laptops", "Tablets", "Cameras", "Audio"],
    "FURNITURE": ["Office", "Living Room", "Bedroom", "Kitchen", "Outdoor"],
    "BOOKS": ["Educational", "Fiction", "Technical", "Business", "Self-Help"],
    "CLOTHING": ["Men's", "Women's", "Children's", "Sports", "Accessories"],
    "FOOD": ["Organic", "Snacks", "Beverages", "Fresh", "Frozen"]
}

PRODUCT_STATUS = [ "AVAILABLE",  "NOT_AVAILABLE",  "PENDING",  "PREORDER",  "EMPTY", "OUT_OF_STOCK"]

DOCUMENT_TYPES = ["USER_MANUAL", "WARRANTY_CARD", "SPECIFICATIONS", "SAFETY_GUIDE",
                 "ASSEMBLY_INSTRUCTIONS", "CARE_GUIDE", "QUICK_START", "COMPLIANCE_CERT"]

@dataclass
class Resource:
    id: str
    description: str

class ProductGenerator:
    def __init__(self):
        self.fake = faker.Faker()

    def generate_resource(self, resource_id: str, description: str) -> Dict:
        return {
            "resourceId": resource_id,
            "value": description
        }

    def generate_categories(self) -> List[Dict]:
        # Pick a random main category and subcategories
        main_category = random.choice(list(PRODUCT_CATEGORIES.keys()))
        subcategories = PRODUCT_CATEGORIES[main_category]
        num_categories = random.randint(1, 3)

        selected_subcategories = random.sample(subcategories, num_categories)
        categories = [
            self.generate_resource(main_category, f"{main_category} Category")
        ]
        categories.extend([
            self.generate_resource(sub, f"{sub} Subcategory")
            for sub in selected_subcategories
        ])
        return categories

    def generate_documents(self) -> List[Dict]:
        num_docs = random.randint(1, 4)
        selected_docs = random.sample(DOCUMENT_TYPES, num_docs)
        return [
            self.generate_resource(doc_type, f"{doc_type.lower().replace('_', '-')}.pdf")
            for doc_type in selected_docs
        ]

    def generate_product(self) -> Dict:
        # Generate a realistic product name and description
        product_type = random.choice(["Smartphone", "Laptop", "Chair", "Book", "Camera", "Desk"])
        name = f"{fake.company()} {product_type} {fake.random_int(1000, 9999)}"

        return {
            "name": name,
            "description": fake.text(max_nb_chars=200),
            "price": round(random.uniform(9.99, 2999.99), 2),
            "status": random.choice(PRODUCT_STATUS),
            "categories": self.generate_categories(),
            "documents": self.generate_documents(),
            "displayImage": f"product_{fake.uuid4()[:8]}.jpg",
            "companyLogo": f"logo_{fake.uuid4()[:8]}.png",
            "contactEmail": fake.company_email(),
            "contactPhone": fake.phone_number(),
            "contactFax": fake.phone_number(),
            "contactWebsite": fake.domain_name(),
            "contactAddress": fake.address().replace('\n', ', ')
        }

def generate_product_data(num_products: int, output_file: str = "product_data.json"):
    """
    Generate random product data and save to JSON file

    Args:
        num_products (int): Number of products to generate
        output_file (str): Output JSON file name
    """
    generator = ProductGenerator()
    products = [generator.generate_product() for _ in range(num_products)]

    with open(output_file, 'w') as f:
        json.dump(products, f, indent=2)

    print(f"Generated {num_products} products and saved to {output_file}")

if __name__ == "__main__":
    # Example usage
    num_products = 10  # Change this number to generate more or fewer products
    generate_product_data(num_products)
