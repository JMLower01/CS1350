#Problem 1


def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.
    Args:
    machines: dict mapping machine name -> log file name
    Returns:
    dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}
    all_lines = []
    for machine in machines:
        error_count = 0
        warning_count = 0
        info_count = 0
        counts[machine] = {}
        with open(machines[machine], "r") as machine_file:
            for line in machine_file:
                if "[ERROR]" in line:
                    error_count += 1
                elif "[WARNING]" in line:
                    warning_count += 1
                elif "[INFO]" in line:
                    info_count += 1
                all_lines.append(f"{machine} | {line.strip()}\n")
        counts[machine]["INFO"] = info_count
        counts[machine]["WARNING"] = warning_count
        counts[machine]["ERROR"] = error_count 
    with open("error.log", "w") as error_file, open("warning.log", "w") as warning_file, open("info.log", "w") as info_file:
        for line in all_lines:
            if "[ERROR]" in line:
                error_file.write(line)
            elif "[WARNING]" in line:
                warning_file.write(line)
            elif "[INFO]" in line:
                info_file.write(line)
    return counts

def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)
    error_count = 0
    warning_count = 0
    info_count = 0
    for machine in counts:
        total_entries = 0
        for entry_type in counts[machine]:
            total_entries += counts[machine][entry_type]
        if counts[machine]["ERROR"] >= 2:
            status = "CRITICAL"
        elif counts[machine]["ERROR"] >= 1 or counts[machine]["WARNING"] >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        error_count += counts[machine]["ERROR"]
        warning_count += counts[machine]["WARNING"]
        info_count += counts[machine]["INFO"]
        print(f"{machine}: {total_entries} entries | INFO {counts[machine]["INFO"]} | WARNING {counts[machine]["WARNING"]} | ERROR {counts[machine]["ERROR"]} | Status: {status}")
    print("-" * 40)
    print(f"Total: {error_count + warning_count + info_count} entries | INFO {info_count} | WARNING {warning_count} | ERROR {error_count}")
    print(f"Errors (see {error_file}):")
    with open(error_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(f"  {line.strip()}")




# Test cases
with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")
with open("server_b.log", "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")
counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)
# {'server_a': {'INFO': 3, 'WARNING': 2, 'ERROR': 1}, 'server_b': {'INFO': 3, 'WARNING': 1, 'ERROR': 2}}
with open("warning.log", "r") as f:
    print(f.read())
# server_a | 2026-10-05 08:03:45 [WARNING] Failed login attempt for user root
# server_a | 2026-10-05 08:03:59 [WARNING] Failed login attempt for user root
# server_b | 2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted
print_report(counts)
# SECURITY LOG REPORT
# ========================================
# server_a: 6 entries | INFO 3 | WARNING 2 | ERROR 1 | Status: NEEDS ATTENTION
# server_b: 6 entries | INFO 3 | WARNING 1 | ERROR 2 | Status: CRITICAL
# ----------------------------------------
# Total: 12 entries | INFO 6 | WARNING 3 | ERROR 3
# Errors (see error.log):
# server_a | 2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures
# server_b | 2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start
# server_b | 2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22


#Problem 2


import json
import pickle
import os

def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []
    with open(csv_file, "r") as file:
        for line in file:
            values = line.strip().split(",")
            if values[0].isdigit():
                incidents.append({"id": values[0], "machine": values[1], "severity": values[2], "description": values[3]})
    return incidents

def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    summary = {}
    summary["total"] = len(incidents)
    summary["by_machine"] = {}
    summary["by_severity"] = {}
    summary["high_ids"] = []
    for entry in incidents:
        summary["by_machine"][entry["machine"]] = 0
        summary["by_severity"][entry["severity"]] = 0
    for entry in incidents:
        summary["by_machine"][entry["machine"]] += 1
        summary["by_severity"][entry["severity"]] += 1
        if entry["severity"] == "high":
            summary["high_ids"].append(entry["id"])
    with open(json_file, "w") as file:
        json.dump(summary, file, indent=2)
    return summary

def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    if not os.path.exists(folder):
        os.mkdir(folder)
    pkl_filepath = os.path.join(folder, "incidents.pkl")
    with open(pkl_filepath, "wb") as file:
        pickle.dump(incidents, file)
    machines = []
    for incident in incidents:
        machines.append(incident["machine"])
    machines = set(machines)
    for machine in machines:
        incident_list = []
        filename = machine + ".json"
        filepath = os.path.join(folder, filename)
        with open(filepath, "w") as machine_file:
            for incident in incidents:
                if incident["machine"] == machine:
                    incident_list.append(incident)
            json.dump(incident_list, machine_file)
    file_list = os.listdir(folder)
    return sorted(file_list)

def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(f"{folder}/incidents.pkl", "rb") as file:
        incident_list = pickle.load(file)
    return incident_list

# Test cases
with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")
incidents = load_incidents("incidents.csv")
print(len(incidents))
# 5
print(incidents[0])
# {'id': 1, 'machine': 'server_a', 'severity': 'high', 'description': 'Account root locked'}
summary = save_summary(incidents, "summary.json")
print(summary)
# {'total': 5, 'by_machine': {'server_a': 2, 'server_b': 3},
# 'by_severity': {'high': 3, 'low': 1, 'medium': 1}, 'high_ids': [1, 2, 5]}
with open("summary.json", "r") as f:
    print(json.load(f) == summary)
    # True
print(archive(incidents, "archive"))
# ['incidents.pkl', 'server_a.json', 'server_b.json']
with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])
    # [1, 4]
restored = load_archive("archive")
print(restored == incidents)
# True
