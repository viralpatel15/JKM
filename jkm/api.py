# Copyright (c) 2023, Finbyz Tech PVT LTD and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import flt


@frappe.whitelist()
def pe_on_submit(self, method):
	fwd_uti(self)

def fwd_uti(self):
	for row in self.get('forwards'):
		target_doc = frappe.get_doc("Forward Contract", row.forward_contract)
		if not frappe.db.get_value("Forward Contract Utilization", filters={"parent": row.forward_contract, "voucher_type": "Payment Entry", "voucher_no": self.name}):
			target_doc.append("payment_entries", {
				"date": self.posting_date,
				"party_type": self.party_type,
				"party": self.party,
				"paid_amount" : row.amount_utilized,
				"voucher_type": "Payment Entry",
				"voucher_no" : self.name,
			})
		target_doc.save()
@frappe.whitelist()
def pe_on_cancel(self, method):
	fwd_uti_cancel(self)
	remove_pe_from_brc(self,method)

def remove_pe_from_brc(self,method):
    voucher_no = self.name
    data = frappe.db.sql(f"""SELECT brc.name as brc , brcp.name
                            from `tabBRC Management` as brc
                            left join `tabBRC Payment` as brcp on brcp.parent = brc.name     
                            where brcp.voucher_type = "Payment Entry" and brcp.voucher_no = '{voucher_no}'
                            """, as_dict=1)

    for row in data:
        frappe.db.delete("BRC Payment",row.name)

def fwd_uti_cancel(self):
	if self.name == "ACC-PAY-2022-00220":pass
	for row in self.get('forwards'):
		doc = frappe.get_doc("Forward Contract", row.forward_contract)
		to_remove = [row for row in doc.payment_entries if row.voucher_no == self.name and row.voucher_type == "Payment Entry"]
		[doc.remove(row) for row in to_remove]
		doc.save()



#Roadtepclaimmanagement