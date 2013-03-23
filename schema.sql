drop table if exists food_items;
create table food_items (
  id integer primary key autoincrement,
  title VARCHAR(255) not null,
  calories INT(11) not null
);

INSERT INTO `food_items` VALUES  
('1', 'Bacon and egg McMuffin', '345'), 
('2', 'Banana milk shake (small)', '205'), 
('3', 'BigMac', '490'), 
('4', 'Cheeseburger', '295'), 
('5', 'Chicken Legend with cool mayonnaise', '550'), 
('6', 'Chicken mayonnaise', '315'), 
('7', 'Chicken McBites', '180'), 
('8', 'Chicken McNugget share box', '835'), 
('9', 'Chocolate milk shake (small)', '205'), 
('10', 'Double cheeseburger', '440'), 
('11', 'Double chocolate muffin', '515'), 
('12', 'Double sausage and egg McMuffin', '520'), 
('13', 'Fillet-o-fish', '335'), 
('14', 'Fish fingers', '195'), 
('15', 'French fries (large)', '460'), 
('16', 'French fries (medium)', '330'), 
('17', 'French fries (small)', '230'), 
('18', 'Fruit bag', '46'), 
('19', 'Garden side salad', '20'), 
('20', 'Grilled chicken salad', '140'), 
('21', 'Grilled chicken salad sandwich', '435'), 
('22', 'Hamburger', '250'), 
('23', 'Hash Brown', '140'), 
('24', 'McChicken sandwich', '385'), 
('25', 'Mozzarella Dippers', '280'), 
('26', 'Pancake and Sausage with syrup', '665'), 
('27', 'Quarterpounder deluxe', '520'), 
('28', 'Quarterpounder deluxe plus bacon', '560'), 
('29', 'Quarterpounder with cheese', '490'), 
('30', 'Sausage and Egg McMuffin', '430'), 
('31', 'Spicy veg wrap', '420'), 
('32', 'Strawberry milk shake (small)', '200');