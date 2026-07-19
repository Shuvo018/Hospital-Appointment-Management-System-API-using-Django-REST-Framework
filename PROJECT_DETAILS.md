

## 1. Authentication (JWT)

JWT Authentication is implemented for all users.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register/` | Register a new patient |
| POST | `/api/login/` | Login and receive JWT token |
| POST | `/api/token/refresh/` | Refresh access token |
| POST | `/api/forgot-password/` | Request password reset |
| POST | `/api/reset-password/` | Reset password |

---

## 2. Profile Management

Every user has the following profile fields:

- Full Name
- Email
- Phone Number
- Address

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profile/` | View logged-in user's profile |
| PUT | `/api/profile/` | Update complete profile |
| PATCH | `/api/profile/` | Update profile partially |

---

## 3. Doctor Management

**Doctor** model fields:

- Name
- Department
- Specialization
- Visiting Fee

**Permissions:**
- Only Admin can create, update, or delete doctors.
- Everyone can view the doctor list.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/doctors/` | View all doctors |
| POST | `/api/doctors/` | Create doctor |
| GET | `/api/doctors/<id>/` | View single doctor |
| PUT | `/api/doctors/<id>/` | Update doctor |
| PATCH | `/api/doctors/<id>/` | Partial update |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

---

## 4. Appointment Management

**Appointment** model fields:

- Patient
- Doctor
- Appointment Date
- Appointment Time
- Status

**Status options:**
- Pending
- Confirmed
- Completed
- Cancelled

**Permissions:**
- Patient can create appointments.
- Patient can view only their own appointments.
- Doctor can view appointments assigned to them.
- Admin can manage all appointments.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/appointments/` | View appointments |
| POST | `/api/appointments/` | Book appointment |
| GET | `/api/appointments/<id>/` | View appointment |
| PUT | `/api/appointments/<id>/` | Update appointment |
| PATCH | `/api/appointments/<id>/` | Update appointment status/details |
| DELETE | `/api/appointments/<id>/` | Cancel/Delete appointment |

---

## 5. Billing

When an appointment is completed, a bill is created.

**Bill** model fields:

- Patient
- Doctor
- Appointment
- Consultation Fee
- Discount
- Total Amount

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/bills/` | View all bills |
| POST | `/api/bills/` | Create bill |
| GET | `/api/bills/<id>/` | View bill |
| PUT | `/api/bills/<id>/` | Update bill |
| PATCH | `/api/bills/<id>/` | Partial update |
| DELETE | `/api/bills/<id>/` | Delete bill |

---

## 6. Dashboard Summary

Returns a summary of hospital statistics.

**Example response includes:**

- Total Patients
- Total Doctors
- Total Appointments
- Pending Appointments
- Completed Appointments

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/dashboard/` | Dashboard summary |

---

## 7. Filtering

**Doctor** — filter by department:

```
GET /api/doctors/?department=Cardiology
```

**Appointment** — filter by status or doctor:

```
GET /api/appointments/?status=Completed
GET /api/appointments/?doctor=2
```

---

## 8. Searching

**Doctor:**

```
GET /api/doctors/?search=Rahman
```

**Appointment** (search by patient name or doctor name):

```
GET /api/appointments/?search=John
```

---

## 9. Ordering

**Doctors:**

```
GET /api/doctors/?ordering=visiting_fee
GET /api/doctors/?ordering=-visiting_fee
```

**Appointments:**

```
GET /api/appointments/?ordering=appointment_date
GET /api/appointments/?ordering=-appointment_date
```

---

## 10. Pagination

10 records per page.

```
GET /api/doctors/?page=2
GET /api/appointments/?page=3
```

---

## 11. Permissions

| User | Permission |
|------|------------|
| Admin | Full access |
| Doctor | View assigned appointments only |
| Patient | Manage only own profile and appointments |


---

## 12. Validation

Basic validations implemented:

- Email must be unique.
- Phone number must be unique.
- Visiting fee cannot be negative.
- Appointment date cannot be in the past.
- Discount cannot be greater than consultation fee.

---

## 13. Postman

All APIs are tested using Postman. The Postman collection includes:

- Authentication APIs
- Profile APIs
- Doctor APIs
- Appointment APIs
- Billing APIs
- Dashboard API

---

## API Endpoint List

See the endpoint tables above for the full list of authentication, profile, doctor, appointment, billing, and dashboard endpoints.

## Postman Collection

An exported Postman collection is included in this repository .