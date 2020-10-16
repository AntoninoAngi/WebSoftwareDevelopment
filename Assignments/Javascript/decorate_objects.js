
function addPersonMethods(person){
    var Persona = {
      name: person.name,
      age: person.age,

      greet : function(string){
        console.log(string + ", my name is " + this.name);
      },
      compareAge : function (Persona){
        if (Persona.age > this.age){
          console.log("My name is " + this.name + " and I'm younger than " + Persona.name);
        }else if (Persona.age < this.age){
          console.log("My name is " + this.name + " and I'm older than " + Persona.name);
        }else{
          console.log("My name is " + this.name + " and I'm equally young as " + Persona.name);
        }
      }
    ,
    namesake : function (Persona){
      if ((this.name).localeCompare(Persona.name) == 0){
        console.log("We have the same name, "+ Persona.name + " and I!");
      }else{
        console.log("We have different names, "+ Persona.name + " and I.");
      }
    }
  }

  return Persona;
}