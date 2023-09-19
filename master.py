import argparse
import subprocess

def start_container(container_names):
    for name in container_names:
        cmd = ['docker-compose', 'up', '-d', name]
        subprocess.Popen(cmd)
        print(cmd)

def start_zebra_ospf(container_names):
    for name in container_names:
        print(name)

def add_routes(routes):
    container, subnet, gateway = routes
    print(container + subnet + gateway)

def north_path():
    print('Hello')

def south_path():
    print('Hello')

def delete_container(container_names):
    for name in container_names:
        print(name)


def main():
    argParser = argparse.ArgumentParser(prog="Lab1-Orchestrator", description="Automates all the docker commands reuired to build docker network for Lab1", epilog="Created by Vatsal Goel")

    argParser.add_argument(
        "-s", 
        "--start_container", 
        help="Starts docker container", 
        nargs= "*")
    argParser.add_argument(
        "-z", 
        "--start_zebra_ospf", 
        help="Copy Zebra & OSPF files to container and start services", 
        nargs= "*")
    argParser.add_argument(
        "-a", 
        "--add_routes", 
        help="Adds routes to the host", 
        nargs= "*")
    argParser.add_argument(
        "-np", 
        "--north_path", 
        help="Directs traffic to North path", 
        nargs= "?")
    argParser.add_argument(
        "-sp", 
        "--south_path", 
        help="Directs traffic to South path", 
        nargs= "?")
    argParser.add_argument(
        "-d", 
        "--delete_container", 
        help="Deletes docker container", 
        nargs= "*")
    
    arg = argParser.parse_args()

    if arg.start_container:
        start_container(arg.start_container)
    elif arg.start_zebra_ospf:
        start_zebra_ospf(arg.start_zebra_ospf)
    elif arg.add_routes:
        add_routes(arg.add_routes)
    elif arg.north_path:
        north_path()
    elif arg.south_path:
        south_path()
    elif arg.delete_container:
        delete_container(arg.delete_container)

    if not any(vars(arg).values()):
        # If no flags are given, prints help and exit
        argParser.print_help()
        return
        

if __name__ == "__main__":
    main()
