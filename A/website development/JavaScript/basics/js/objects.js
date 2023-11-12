const product = {
      name: 'sock',
      price: 1000,
      'tax-price': '10%',
      rating: {
        stars: 4.5,
        count: 87,
      },
      fun: function function1() {
        console.log("this is function inside object")
      }
    };
    
    console.log(product);
    console.log(product.name)
    console.log(product.price)
    
    product.name = 'cotton sock'
    console.log(product.name)
    
    product.newProperty = 'soft sock'
    console.log(product.newProperty)
    
    delete product.newProperty
    console.log(product.newProperty)
    
    console.log(product ['name'])
    console.log(product['tax-price'])
    
    console.log(product.rating.stars)
    console.log(product.rating.count)
    
    product.fun()
    
    
    
    
    
    
    console.log(JSON.stringify(product))
    
    const json = JSON.stringify(product)
    console.log(JSON.parse(json))
    
    
    
    
    
    
    
    

 const object1 = {
      message: 'hello'
    };
   
    console.log(object1)
    
    const object2 = object1;
    console.log(object2)
    
    const object3 = {
      message: 'hello'.length
    }
    
    console.log(object3.message)
    
    object1.message = 'nice';
    
    console.log(object3 === object1)
    console.log(object2 === object1)
    console.log(object1)
    
    
    
    
    
    
    
    
    const object4 = {
      name: 'SHORT'.toLowerCase(),
      price: 1000000,
      
      method() {
        console.log('method'.toUpperCase())
      }
    };
    
    const { name, price } = object4;  
    console.log(name,price);
    
    object4.method();
    
    const object5 = {
      name
    };
    
    console.log(object4)
    console.log(object5);
    