import frappe
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def create_costing_details(source_name, target_doc=None):
	doclist = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
				"doctype": "Costing Details",
				"field_map": { "name": "opportunity"},
			},
			"Opportunity Item": {
				"doctype": "Supplier Quotation Item",
				"field_map": {
					"uom": "stock_uom",
				},
			},
		},
		target_doc,
	)

	return doclist