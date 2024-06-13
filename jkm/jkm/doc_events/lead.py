import frappe
from frappe.utils import get_link_to_form, now
from frappe.desk.form.assign_to import add as add_assignment


def validate(self, method):
    data = frappe.db.sql(f"""
            Select name
            From `tabLead`
            where status not in ('Opportunity', 'Quotation') and custom_item_group = '{self.custom_item_group}'
            and (email_id = '{self.email_id}' or custom_mobile_number = '{self.custom_mobile_number}')
    """, as_dict = 1)

    if data:
        message = "Inquiry is allready exist in the system for item group <b>{0}</b> please check the link mentioned below".format(self.custom_item_group)
        for row in data:
            message += "<p>{0}</p>".format(get_link_to_form("Lead" , row.name))
            
        frappe.throw(str(message))
def after_insert(self, method):
    events = frappe.db.sql(f"""
        Select e.name
        From `tabEvent` as e
        Left join `tabEvent Participants` as ep ON e.name = ep.parent
        Where ep.reference_docname = '{self.name}' and ep.reference_doctype = 'Lead'
    """,as_dict = 1)
    if not events:
        doc = frappe.new_doc("Event")
        subject = "Company Name : {0}\n<br>".format(self.company_name)
        subject += "Item Group : {0}\n<br>".format(self.custom_item_group)
        subject += "Name : {0}\n<br>".format(self.first_name)
        subject += "Email : {0}\n<br>".format(self.email_id)
        subject += "Mobile No : {0}\n<br>".format(self.custom_mobile_number)
        doc.subject = subject
        doc.event_category = "Call"
        doc.event_type = "Public"
        doc.starts_on = now()
        doc.status = "Open"
        doc.append("event_participants",{
            "reference_doctype":"Lead",
            "reference_docname":self.name
        })
        doc.insert()
