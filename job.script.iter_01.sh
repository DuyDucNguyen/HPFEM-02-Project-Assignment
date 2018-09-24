# mesh0.bin is the starting mesh
#cp mesh0.bin mesh.bin

M=32
MMAX=128

mkdir -p iter_01
( mpirun -n 3 ./cube > log1 2> log2 < /dev/null )

mpirun -n 3 ./dolfin_post -m mesh_out.bin -t vtk -n 1000 -s velocity -f 1  1> log.pp1 2> log.ppe1
mpirun -n 3 ./dolfin_post -m mesh_out.bin -t vtk -n 1000 -s dvelocity -f 1  1> log.pp2 2> log.ppe2
mpirun -n 3 ./dolfin_post -m mesh_out.bin -t vtk -n 1000 -s pressure -f 1 1> log.pp3 2> log.ppe3
mpirun -n 3 ./dolfin_post -m mesh_out.bin -t vtk -n 1000 -s dpressure -f 1 1> log.pp4 2> log.ppe4

mv *.bin log1 log2 *.vtu *.pvd iter_01

cp iter_01/rmesh.bin iter_01/mesh0.bin iter_01/log1 iter_01/log2 .
cp rmesh.bin mesh.bin

