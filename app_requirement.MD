
### BT Real Estate App Requirements


#### FRONTEND PAGES
- Home
- About
- Listings
- Single Listing
- Search
- Register
- Login
- Dashboard (Inquiries)

#### DESIGN SPECS
- Use BTRE logo (Frontend and admin)
- Branding colors – blue(#10284e) green(#30caa0)
- Mobile Friendly
- Social media icons & contact info
- Doesn’t have to be too fancy but must be clean


#### FUNCTIONALITY SPECS
- Manage listings, realtors, contact inquiries and website users via admin
- Role based users (staff and non-staff)
- Display listings in app with pagination
- Ability to set listings to unpublished
- Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
- List realtors on about page with “seller of the month” (Control via admin)
- Listing page should have fields listed below
- Listing page should have 5 images with lightbox
- Lightbox should scroll through images
- Listing page should have a form to submit inquiry for that property listing
- Form info should go to database and notify realtor(s) with an email
- Frontend register/login to track inquiries
- Both unregistered and registered users can submit form. If registered, can only submit one per listing



#### LISTING PAGE FIELDS
- Title
- Address, city, state, zip
- Price
- Bedrooms
- Bathrooms
- Square Feet
- Lot Size
- Garage
- Listing Date
- Realtor – Name & Image
- Main image and 5 other images

#### Possible Future Functionality
- Google maps on listing page
- Buyer testimonials


### DATA MODEL
####LISTING
- id: INT
- realtor: Object {}
  - id: PK
  - name: STR
  - photo: STR
  - description: STR
  - email: STR
  - phone: STR
  - is_mvp: BOOL [0]
  - hire_date: DATE
- title: STR
- address: STR
- city: STR
- state: STR
- zipcode: STR
- description: TEXT
- price: INT
- bedroom: INT
- bathrooms: INT
- garage: INT [0]
- sqft: INT
- lot_size: FLOAT
- is_published: BOOL [true]
- list_date: DATE
- photo: Object {}
  - photo_main
  - photo_1
  - photo_2
  - photo_3
  - photo_4...

#### CONTACT
- id: INT
- user_id: INT
- listing: INT
- listing_id: INT
- name: STR
- email: STR
- phone: STR
- message: TEXT
- contact_date: DATE