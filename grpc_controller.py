"""
Usage:
    controller.py <file>  [-k|--kill] [-s|--start]

Arguments:
    file                    The csv file with information of servers

Options:
    -s --start              Start reporters on servers
    -k --kill               Kill all reporters on servers
"""
import docopt
import os


def get_ip():
    result = os.popen("ifconfig | grep addr:10")
    ips = result.read().strip().split()
    for each in ips:
        if each[:5] == "addr:":
            return 0, each[5:]
    return 0, "0.0.0.0"


def update_with_screen(work_servers, kill=False):
    with open(work_servers, "r")as fin:
        lines = fin.readlines()
    for each in lines[1:]:
        data = each.strip().split(",")
        with open("run.sh", "w") as fout:
            cmd = f"""#!/usr/bin/expect
            set host {data[0]}
            set user {data[1]}
            set timeout 10
            
            spawn ssh $user@$host
            expect "*password:*"
            send "{data[2]}\\r"
            expect "*]#"
            send "screen -S gpu_reporter -X quit\\r"
            expect "*]#"
            """
            if not kill:
                cmd += f"""send "screen -S gpu_reporter\\r"
                expect "*]#"
                send "cd gpustat\\r"
                expect "*]#"
                send "python main.py -r {base_url}\\r"
                expect "*]#"
                send "exit\\r"
                expect eof"""
            fout.write(cmd)
        os.system("chmod 777 run.sh && ./run.sh")
        print(f"\n====={data[0]}, ok!=====\n")
    os.system("rm run.sh")


if __name__ == "__main__":
    err, ip = get_ip()
    if err > 0:
        print("Can't get the IP address.")
    else:
        base_url = ip
        args = docopt.docopt(__doc__, version='GPU Info Controller v2.0')
        if args['--start']:
            update_with_screen(args['<file>'])
        elif args['--kill']:
            update_with_screen(args['<file>'], True)
        else:
            print(__doc__)
