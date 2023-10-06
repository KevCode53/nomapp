import {
  axiosPrivateInstance,
  axiosPublicInstance,
} from "../utilitys/axios-instances";
import { loadAbort } from "../utilitys/load-abort-axios.utility";

const baseUrl = "api/";
const employeesUrl = "http://localhost:8000/api/employees/";

export const getEmployees = () => {
  const controller = loadAbort();
  return {
    call: axiosPrivateInstance.get(employeesUrl, { signal: controller.signal }),
    controller,
  };
};

export const getEmployeesFilter = (companyID) => {
  const controller = loadAbort();
  return {
    call: axiosPrivateInstance.get(
      `http://localhost:8000/api/employees-filter/?companyId=${companyID}`,
      { signal: controller.signal }
    ),
    controller,
  };
};

export const getOneEmployee = (id) => {
  const controller = loadAbort();
  return {
    call: axiosPublicInstance.get(`http://localhost:8000/api/employees/${id}`, {
      signal: controller.signal,
    }),
    controller,
  };
};

export const addEmployee = (data) => {
  const controller = loadAbort();
  return {
    call: axiosPrivateInstance.post(
      `http://localhost:8000/api/employees/`,
      data,
      { signal: controller.signal }
    ),
    controller,
  };
};

export const checkPayments = (employee, querys) => {
  const url = `http://127.0.0.1:8000/api/check-payment/${employee}/?${querys}`;
  const controller = loadAbort();
  return {
    call: axiosPrivateInstance.get(url, {
      signal: controller.signal,
    }),
    controller,
  };
};

export const downloadTicket = (type, id) => {
  const url = `http://127.0.0.1:8000/api/payment-ticket-pdf/${id}/?type=${type}`;
  const controller = loadAbort();
  return {
    call: axiosPrivateInstance.get(url, {
      signal: controller.signal,
    }),
    controller,
  };
};
