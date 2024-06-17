
frappe.ui.form.on("Opportunity", {
    refresh:frm=>{
        frm.add_custom_button(
            __("Costing Details"),
            function () {
                frm.trigger("create_costing_details");
            },
            __("Create")
        );
    },
    create_costing_details:frm =>{
        frappe.model.open_mapped_doc({
			method: "jkm.jkm.doc_events.supplier_quotation.create_costing_details",
			frm: cur_frm,
		});
    }
})