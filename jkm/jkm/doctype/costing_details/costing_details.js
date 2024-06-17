// Copyright (c) 2024, viral@fosserp.com and contributors
// For license information, please see license.txt

frappe.ui.form.on("Costing Details", {
    refresh:frm=>{
        frm.set_query("items_quotation", function () {
			return {
				filters: {
					docstatus: 1,
				},
			};
		});
        frm.set_query("supplier_quotation", function () {
			return {
				filters: {
					docstatus: 1,
                    supplier:frm.doc.supplier
				},
			};
		});
    },
    items_quotation:frm=>{
        if(frm.doc.items_quotation){
            frappe.call({
                method:"jkm.jkm.doctype.costing_details.costing_details.get_item_details",
                args:{
                    docname : frm.doc.items_quotation
                },
                callback:e=>{
                    frm.doc.items = []
                    e.message.items.forEach(element => {
                        let row = frm.add_child("items");
                        row.amount = element.amount
                        row.base_amount = element.base_amount
                        row.base_net_amount = element.base_net_amount
                        row.base_net_rate = element.base_net_rate
                        row.base_price_list_rate = element.base_price_list_rate
                        row.base_rate = element.base_rate
                        row.cess_amount = element.cess_amount
                        row.cess_non_advol_amount = element.cess_non_advol_amount
                        row.cess_non_advol_rate = element.cess_non_advol_rate
                        row.cess_rate = element.cess_rate
                        row.cgst_amount = element.cgst_amount
                        row.cgst_rate = element.cgst_rate
                        row.conversion_factor = element.conversion_factor
                        row.cost_center = element.cost_center
                        row.description =element.description
                        row.discount_amount=element.discount_amount
                        row.discount_percentage= element.discount_percentage
                        row.gst_hsn_code = element.gst_hsn_code
                        row.igst_amount = element.igst_amount
                        row.igst_rate =element.igst_rate
                        row.is_free_item = element.is_free_item
                        row.is_ineligible_for_itc = element.is_ineligible_for_itc
                        row.item_code = element.item_code
                        row.item_group = element.item_group
                        row.item_name = element.item_name
                        row.item_tax_rate = element.item_tax_rate
                        row.item_tax_template = element.item_tax_template
                        row.lead_time_days = element.lead_time_days
                        row.net_amount = element.net_amount
                        row.net_rate = element.net_rate
                        row.pricing_rules = element.pricing_rules
                        row.qty = element.qty
                        row.rate = element.rate
                        row.sgst_amount=element.sgst_amount
                        row.sgst_rate=element.sgst_rate
                        row.stock_qty=element.stock_qty
                        row.stock_uom=element.stock_uom
                        row.taxable_value=element.taxable_value
                        row.total_weight=element.total_weight
                        row.uom=element.uom
                        row.warehouse= element.warehouse
                        row.weight_per_unit=element.weight_per_unit
                        frm.refresh_field("items");
                    });
                    frm.set_value('total_quantity', e.message.total_qty)
                    frm.set_value('total_amount', e.message.total)
                    frm.set_value('total_taxes_and_charges_d', e.message.total_taxes_and_charges)
                    frm.set_value('grand_total_d', e.element.grand_total)
                }
            })
        }
    },
    supplier_quotation:frm=>{
        if(frm.doc.supplier_quotation){
            frappe.call({
                method:"jkm.jkm.doctype.costing_details.costing_details.get_item_details",
                args:{
                    docname : frm.doc.supplier_quotation
                },
                callback:e=>{
                    frm.doc.items = []
                    e.message.items.forEach(element => {
                        let row = frm.add_child("shipping_charges");
                        row.amount = element.amount
                        row.base_amount = element.base_amount
                        row.base_net_amount = element.base_net_amount
                        row.base_net_rate = element.base_net_rate
                        row.base_price_list_rate = element.base_price_list_rate
                        row.base_rate = element.base_rate
                        row.cess_amount = element.cess_amount
                        row.cess_non_advol_amount = element.cess_non_advol_amount
                        row.cess_non_advol_rate = element.cess_non_advol_rate
                        row.cess_rate = element.cess_rate
                        row.cgst_amount = element.cgst_amount
                        row.cgst_rate = element.cgst_rate
                        row.conversion_factor = element.conversion_factor
                        row.cost_center = element.cost_center
                        row.description =element.description
                        row.discount_amount=element.discount_amount
                        row.discount_percentage= element.discount_percentage
                        row.gst_hsn_code = element.gst_hsn_code
                        row.igst_amount = element.igst_amount
                        row.igst_rate =element.igst_rate
                        row.is_free_item = element.is_free_item
                        row.is_ineligible_for_itc = element.is_ineligible_for_itc
                        row.item_code = element.item_code
                        row.item_group = element.item_group
                        row.item_name = element.item_name
                        row.item_tax_rate = element.item_tax_rate
                        row.item_tax_template = element.item_tax_template
                        row.lead_time_days = element.lead_time_days
                        row.net_amount = element.net_amount
                        row.net_rate = element.net_rate
                        row.pricing_rules = element.pricing_rules
                        row.qty = element.qty
                        row.rate = element.rate
                        row.sgst_amount=element.sgst_amount
                        row.sgst_rate=element.sgst_rate
                        row.stock_qty=element.stock_qty
                        row.stock_uom=element.stock_uom
                        row.taxable_value=element.taxable_value
                        row.total_weight=element.total_weight
                        row.uom=element.uom
                        row.warehouse= element.warehouse
                        row.weight_per_unit=element.weight_per_unit
                        frm.refresh_field("shipping_charges");
                    });
                    frm.set_value('total_amount_domestic', e.message.total)
                    frm.set_value('taxes_and_charges', e.message.total_taxes_and_charges)
                    frm.set_value('grand_total', e.element.grand_total)
                }
            })
        }
    }
});


