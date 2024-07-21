const inventory = [
   { id: 1, car_make: "Lincoln", car_model: "Navigator", car_year: 2009 },
   { id: 2, car_make: "Mazda", car_model: "Miata MX-5", car_year: 2001 },
   { id: 3, car_make: "Honda", car_model: "Accord", car_year: 1983 },
   { id: 4, car_make: "Land Rover", car_model: "Defender Ice Edition", car_year: 2010 },
   { id: 5, car_make: "Honda", car_model: "Accord", car_year: 1995 },
 ];

 function getHondaCar(car_inventory){
   let hondaCar = car_inventory.filter(car => car.car_make === "Honda")

   if (hondaCar){
      const {car_make, car_model, car_year} = hondaCar
      return `This is a ${car_make} ${car_model} from the year ${car_year}`
   }
   else {
      return "no honda car found"
   }
 }

 function sortCarInventoryByYear(car_inventory){
   return car_inventory.sort((a, b) => a.car_year - b.car_year)
 }