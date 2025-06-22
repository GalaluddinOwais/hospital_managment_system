# 👇 VIDEO DEMONSTRATION HERE 👇 
[Video Recording Drive link](https://drive.google.com/drive/folders/1K2XcRBoRogcwz3t2jXfMacQjeTOSVbKZ)

(I am working on the screenshots) - until then, please accept my video demonstration (You can play it on x2)

# Hospital Management System (HMS)

This is a custom Odoo module for managing hospital operations, including patients, doctors, departments, and patient logs.

## Features

- **Patient Management:** Register, update, and track patients, including medical history, PCR, blood type, and department assignment.
- **Doctor Management:** Manage doctors, their departments, and assigned patients.
- **Department Management:** Create and manage hospital departments, their capacity, and status.
- **Patient Logs:** Automatic logging of patient state changes.
- **Access Control:** User and Manager groups with different permissions.
- **Reporting:** Generate PDF reports for patients.
- **CRM Integration:** Link patients to CRM customers.

## Installation

1. Copy the `hms` folder to your Odoo `custom_addons` directory.
2. Ensure adding the folder path to the addons_path variable in your odoo.conf file.
3. Update the app list in Odoo and upgrade the 'hospital management system' module.
4. Install the "Hospital Management System" module from the Apps menu.

## Usage

- Access the HMS menu from the main Odoo dashboard.
- Manage Patients, Doctors, and Departments from their respective menus.
- Only users in the "HMS Manager" group can create, edit, or delete doctors and departments.
- Generate patient reports from the patient form view.

## Security

- HMS User and HMS Manager groups with record rules and access rights.
- Only managers can delete records and view doctors; users have limited write access and can view patients they created only.
