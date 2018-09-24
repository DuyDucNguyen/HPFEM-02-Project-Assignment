# Download
sudo apt-get update
sudo apt-get install singularity-container git

# Download image
wget http://www.csc.kth.se/~jjan/mooc-hpfem/mso4sc-fenics-unicorn-latest.simg

# Activate singularity
singularity shell mso4sc-fenics-unicorn-latest.simg

# Create unicorn
git clone https://bitbucket.org/fenics-hpc/unicorn.git

cd unicorn

# Run before execution
git fetch --all

# download branch named "next"
#git checkout next

export UNICORNLIBDIR=$PWD

# Make execution file
make -j 3

# Remove old execution file
make clean

# Make test folder
mkdir test01

# Copy files to the test folder
cp cube test01
cp mesh0.bin test01/mesh.bin
cp dolfin_post test01
cp mesh0.bin test01
cd test01

# Activate dolfin_post
chmod +x dolfin_post

# Run job_script.sh
sh job_script.sh

# convert bin into vtk
./dolfin_post -m mesh_out.bin -t vtk -n 200 -s velocity -f 10

# Measure mean drag force
grep -a "mean drag" log1



