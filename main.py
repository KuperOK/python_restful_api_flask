from app import app
from app import db
import views.view
import rest.api_dept
import rest.api_emp
import models.models


if __name__ == "__main__":
    app.run(debug=True)
