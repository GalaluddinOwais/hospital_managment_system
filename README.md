# DEMONSTRATION !!!!!
[Video Recording Drive link]([/guides/content/editing-an-existing-page#modifying-front-matter](https://drive.google.com/drive/folders/1K2XcRBoRogcwz3t2jXfMacQjeTOSVbKZ))


# Hospital Management System (HMS)

This is a custom Odoo module for managing hospital operations, including patients, doctors, departments, and patient logs.

## Features

- **Patient Management:** Register, update, and track patients, including medical history, PCR, blood type, and department assignment.
- **Doctor Management:** Manage doctors, their departments, and assigned patients.
- **Department Management:** Create and manage hospital departments, their capacity, and status.
- **Patient Logs:** Automatic logging of patient state changes.
- **Access Control:** User and Manager groups with different permissions.
- **Reporting:** Generate PDF reports for patients.
- **CRM Integration:** Link patients to CRM partners.

## Installation

1. Copy the `hms` folder to your Odoo `custom_addons` directory.
2. Update the app list in Odoo.
3. Install the "Hospital Management System" module from the Apps menu.

## Usage

- Access the HMS menu from the main Odoo dashboard.
- Manage Patients, Doctors, and Departments from their respective menus.
- Only users in the "HMS Manager" group can create, edit, or delete doctors and departments.
- Generate patient reports from the patient form view.

## File Structure

- `models/`: Python models for patients, doctors, departments, logs, and partner inheritance.
- `views/`: XML views for forms, lists, and menus.
- `reports/`: QWeb templates for patient reports.
- `security/`: Access rights and group definitions.
- `__manifest__.py`: Module manifest.

## Security

- HMS User and HMS Manager groups with record rules and access rights.
- Only managers can delete records; users have limited write access.

## Author

Galaluddin

---

For any issues or contributions, please open an issue or pull request.
