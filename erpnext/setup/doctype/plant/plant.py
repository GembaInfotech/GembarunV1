# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Plant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		billing_address: DF.Data | None
		company: DF.Link | None
		contact: DF.Data | None
		establishment_date: DF.Date | None
		gstin: DF.Data | None
		is_group: DF.Check
		item: DF.Link | None
		lft: DF.Int
		old_parent: DF.Link | None
		parent_plant: DF.Link | None
		plant_name: DF.Data | None
		rgt: DF.Int
		shipping_address: DF.Data | None
	# end: auto-generated types
	pass
