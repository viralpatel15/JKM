import frappe
from frappe.utils import get_link_to_form


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