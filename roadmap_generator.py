# Define a learning roadmap for commonly missing technical skills.
LEARNING_ROADMAP = {

    # Define the roadmap for Docker.
    "docker": {
        "level": "Beginner",
        "topics": [
            "Docker basics",
            "Images and containers",
            "Dockerfile",
            "Docker Compose"
        ]
    },

    # Define the roadmap for PyTorch.
    "pytorch": {
        "level": "Beginner",
        "topics": [
            "PyTorch tensors",
            "Datasets and DataLoaders",
            "Neural networks",
            "Model training"
        ]
    },

    # Define the roadmap for Deep Learning.
    "deep learning": {
        "level": "Beginner",
        "topics": [
            "Neural networks",
            "Activation functions",
            "Loss functions",
            "Backpropagation",
            "Model optimization"
        ]
    },

    # Define the roadmap for Pandas.
    "pandas": {
        "level": "Beginner",
        "topics": [
            "Series and DataFrames",
            "Data cleaning",
            "Filtering and sorting",
            "GroupBy operations",
            "Data analysis"
        ]
    },

    # Define the roadmap for NumPy.
    "numpy": {
        "level": "Beginner",
        "topics": [
            "NumPy arrays",
            "Array indexing",
            "Array operations",
            "Broadcasting",
            "Numerical computations"
        ]
    },

    # Define the roadmap for SQL.
    "sql": {
        "level": "Beginner",
        "topics": [
            "SELECT queries",
            "WHERE and ORDER BY",
            "GROUP BY",
            "JOIN operations",
            "Subqueries"
        ]
    },

    # Define the roadmap for Matplotlib.
    "matplotlib": {
        "level": "Beginner",
        "topics": [
            "Basic plots",
            "Line and bar charts",
            "Labels and titles",
            "Subplots",
            "Data visualization"
        ]
    },

    # Define the roadmap for Transformers.
    "transformers": {
        "level": "Intermediate",
        "topics": [
            "Transformer architecture",
            "Attention mechanism",
            "Tokenization",
            "Pre-trained models",
            "Fine-tuning"
        ]
    },

    # Define the roadmap for Hugging Face.
    "hugging face": {
        "level": "Beginner",
        "topics": [
            "Hugging Face Hub",
            "Transformers library",
            "Tokenizers",
            "Pre-trained models",
            "Model pipelines"
        ]
    },

    # Define the roadmap for LLM.
    "llm": {
        "level": "Beginner",
        "topics": [
            "LLM fundamentals",
            "Tokens and embeddings",
            "Prompt engineering",
            "Context windows",
            "LLM applications"
        ]
    },

    # Define the roadmap for RAG.
    "rag": {
        "level": "Intermediate",
        "topics": [
            "Document loading",
            "Text chunking",
            "Embeddings",
            "Vector databases",
            "Retrieval and generation"
        ]
    },

    # Define the roadmap for FastAPI.
    "fastapi": {
        "level": "Beginner",
        "topics": [
            "API fundamentals",
            "FastAPI routes",
            "Request and response handling",
            "Pydantic models",
            "API deployment"
        ]
    },

    # Define the roadmap for Flask.
    "flask": {
        "level": "Beginner",
        "topics": [
            "Flask basics",
            "Routes",
            "Request handling",
            "Templates",
            "REST APIs"
        ]
    },

    # Define the roadmap for MongoDB.
    "mongodb": {
        "level": "Beginner",
        "topics": [
            "NoSQL fundamentals",
            "Documents and collections",
            "CRUD operations",
            "Queries",
            "Indexes"
        ]
    },

    # Define the roadmap for PostgreSQL.
    "postgresql": {
        "level": "Beginner",
        "topics": [
            "PostgreSQL basics",
            "Tables and relationships",
            "SQL queries",
            "Indexes",
            "Database management"
        ]
    },

    # Define the roadmap for REST API.
    "rest api": {
        "level": "Beginner",
        "topics": [
            "HTTP methods",
            "API endpoints",
            "Request and response",
            "JSON",
            "API authentication"
        ]
    }
}


# Define a function to generate a learning roadmap.
def generate_roadmap(missing_skills):

    # Create an empty list to store the learning roadmap.
    roadmap = []

    # Loop through every missing skill.
    for skill in missing_skills:

        # Convert the skill name to lowercase for dictionary lookup.
        skill_key = skill.lower()

        # Check whether a roadmap exists for the skill.
        if skill_key in LEARNING_ROADMAP:

            # Get the roadmap information for the skill.
            roadmap_item = LEARNING_ROADMAP[skill_key]

            # Create a structured roadmap entry.
            roadmap.append({
                "skill": skill,
                "level": roadmap_item["level"],
                "topics": roadmap_item["topics"]
            })

        # Handle skills that do not have a predefined roadmap.
        else:

            # Add a basic roadmap entry for the unknown skill.
            roadmap.append({
                "skill": skill,
                "level": "Beginner",
                "topics": [
                    "Learn the fundamentals",
                    "Practice basic concepts",
                    "Build a small project"
                ]
            })

    # Return the complete learning roadmap.
    return roadmap