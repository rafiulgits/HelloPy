### GraphQL - Django

#### Setup
 ```
 >> pip3 install requirements.txt

 >> python manage.py runserver

 ```

#### Run
 Open browser `localhost:8000/graphql`

```
query {
  allOrders {
    id
    ammount
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
  
  allProducts {
    code
    name
    price
  }
  
  
  allCustomers(name_Icontains:" ") {
    edges {
      node {
        name
        phone
      }
    }
  }
  
  customer(id:"Q3VzdG9tZXJUeXBlOjQ="){
    name
    phone
    email
  }
  
  
}
```

### [Official Doc](https://docs.graphene-python.org/projects/django/en/latest/)