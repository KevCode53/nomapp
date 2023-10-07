import {
  axiosPrivateInstance,
  axiosPublicInstance,
} from "../utilitys/axios-instances";
import { loadAbort } from "../utilitys/load-abort-axios.utility";

const productssUrl = "api/products/";

export const getProducts = () => {
  const controller = loadAbort();
  return {
    call: axiosPublicInstance.get(productssUrl, {
      signal: controller.signal,
    }),
    controller,
  };
};
