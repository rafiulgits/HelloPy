### GraphQL - Djano

#### Setup
 ```
 	pip3 install requirements.txt

 	python manage.py runserver

 ```

#### Run
 Open browser `localhost:8000/graphql`


```
	query {
	  allOrders {
	    id 
	    product {
	      name
	      code
	      price
	    }
	    customer {
	      name
	      phone
	      email
	    }
	  }
	}
```
