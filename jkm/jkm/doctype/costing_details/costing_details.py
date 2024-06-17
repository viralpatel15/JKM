# Copyright (c) 2024, viral@fosserp.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CostingDetails(Document):
	def validate(self):
		if self.items_quotation:
			doc = frappe.get_doc("Supplier Quotation", self.items_quotation)
			self.items = []
			for row in doc.items:
				self.append('items', row)
		total_qty = 0
		taxable_value = 0
		net_amount = 0
		for row in self.items:
			total_qty += row.qty
			net_amount += row.amount
			taxable_value += row.taxable_value
		self.total_quantity = total_qty
		self.total_amount = net_amount
		self.taxable_value = taxable_value

@frappe.whitelist()		
def get_item_details(docname):
	return frappe.get_doc("Supplier Quotation", docname)