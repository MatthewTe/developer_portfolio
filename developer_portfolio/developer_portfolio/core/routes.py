# Importing Flask Blueprinting Modules:
from flask import Blueprint, render_template
from flask import current_app as app

# Importing Notion API methods:
import notion
from notion.client import NotionClient

# Importing 3rd party packages: 
from datetime import datetime
import os

# Blueprink Configuration:
core_bp = Blueprint(
    "core_bp", __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/core"
)

# Utility function that queries Notion API:
def get_reviews(media_type, **kwargs):
    # Creating conneciton to Notion Client and specific article page:
    client = NotionClient(token_v2=os.environ["TOKEN_V2"])
    readings_page = client.get_block(os.environ["PAGE_URL"])
    
    # Trying to unpack kwargs:
    media_category = kwargs.get("media_category", None)
    
    # Extracting the main table block. This table is named 'readings':
    for child in readings_page.children:
        if child.title == "Readings":
            
            # Extracting the readings table as a collection object:
            collection = client.get_collection(child.collection.id)
            reading_tbl = collection.get_rows()
            
            # Only extracting reviews that have been marked as 'finished' that are correct review type:
            reviews = [] # Empty lst to be populated w reviews then turned into JSON object
            for row in reading_tbl:
                if media_category is not None:
                    if row.status == "Finished" and row.Type == media_type and row.Category == media_category:
                        
                        # Seralizing this information into JSON objects:
                        review = {
                            "Name":row.Name,
                            "Type":row.Type,
                            "Author":", ".join(row.Author),
                            "Category":row.Sub_Category,
                            "Publisher":row.Publisher,
                            "Published": row.Publishing_Release_Date.start.strftime("%m/%d/%Y"),
                            "Full_Page":row.Review_Url,
                            "link":row.link,
                        }

                        reviews.append(review)
                
                # If no media category is provided then query all reviews of the same media type:
                else: 
                    if row.status == "Finished" and row.Type == media_type:   
                        # Seralizing this information into JSON objects:
                        review = {
                            "Name":row.Name,
                            "Type":row.Type,
                            "Author":", ".join(row.Author),
                            "Category":row.Sub_Category,
                            "Publisher":row.Publisher,
                            "Published": row.Publishing_Release_Date.start.strftime("%m/%d/%Y"),
                            "Full_Page":row.Review_Url,
                            "link":row.link,
                        }

                        reviews.append(review)

        
            return reviews

@core_bp.route("/", methods=["GET"])
def portfolio_home():
    """
    View that renders the front end of the portfolio's homepage.
    """
    return render_template("home.html")
    
@core_bp.route("/velkozz_project", methods=["GET"])
def velkozz_project():
    """
    The View that renders the template for the Velkozz Django Rest Framework Project. 
    """
    return render_template("velkozz_project.html")

@core_bp.route("/esg_papers", methods=["GET"])
def esg_papers():
    """
    The View that renders the front-end for all ESG Research Papers.
    """
    esg_papers = get_reviews("Academic Journal", media_category="ESG_Papers")

    return render_template("esg_papers.html", esg_papers=esg_papers)

@core_bp.route("/policy_papers", methods=["GET"])
def policy_papers():
    """
    The View that renders the front-end for all Policy Research Papers.
    """
    policy_papers = get_reviews("Academic Journal", media_category="Policy_Papers")

    return render_template("policy_papers.html", policy_papers=policy_papers)

@core_bp.route("/ml_paper_implementations", methods=["GET"])
def ml_implementations():
    """
    The View that renders the front-end for all Machine Learning research paper implementations.
    """
    ml_papers = get_reviews("Academic Journal", media_category="ML_Papers")

    return render_template("ml_papers.html", ml_papers=ml_papers)

@core_bp.route("/book_reviews", methods=["GET"])
def book_reviews():
    """
    The View that renders the front-end for all Book Reivews that I have done
    """
    book_reviews = get_reviews("Book")

    return render_template("book_reviews.html")