gridSize=60;

numberOfLengths=1;
numberOfWidth=2;

length=(gridSize*numberOfLengths);
width=(gridSize*numberOfWidth);
height=65;
bottom_thickness=1;
wall_thickness=1;

translate([-(length/2),-(width/2),0]){
    cube([length,width,bottom_thickness]);
}

translate([-(length/2),-(width/2),0]){
    cube([length,wall_thickness,height]);
}

translate([-(length/2),(width/2-wall_thickness),0]){
    cube([length,wall_thickness,height]);
}

translate([-(length/2),(-width/2),0]){
    cube([wall_thickness,width,height]);
}

translate([(length/2-wall_thickness),(-width/2),0]){
    cube([wall_thickness,width,height]);
}