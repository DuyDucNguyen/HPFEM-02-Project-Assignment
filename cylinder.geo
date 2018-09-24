//+
SetFactory("OpenCASCADE");

// X,Y,Z, DX, DY, DZ Radius, Angle
cx = -10.0;
cy = 0.0;
cz = 0.0;
cr = 10.0;

cxmax = 40.0;

Cylinder(1) = {cx, cy, cz, cxmax, 0, 0, cr, 2*Pi};

bx = -1.0;
by = 0.0; 
bz = 0.0; 
bxmax = 2.0;
br = 0.5;

Cylinder(2) = {bx, by, bz, bxmax, 0, 0, br, 2*Pi};


//+
BooleanDifference{ Volume{1}; Delete; }{ Volume{2}; Delete; }

// Box field
Field[1] = Box;
Field[1].VIn = 0.1;
Field[1].VOut = 2;

Field[1].XMax = 1;
Field[1].XMin = -1;
Field[1].YMax = 1;
Field[1].YMin = -1;
Field[1].ZMax = 1;
Field[1].ZMin = -1;

Background Field = 1;

