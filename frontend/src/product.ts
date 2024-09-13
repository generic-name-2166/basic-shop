interface Product {
  name: string;
  description: string;
  price: number;
}

const api = "/api/products/";

async function getProducts(): Promise<Product[]> {
  return fetch(api)
    .then((res) => res.json())
    .catch((err) => (console.error(err), [])) as Promise<Product[]>;
}

function createProduct({ name, description, price }: Product): HTMLDivElement {
  const div = document.createElement("div");
  div.classList.add("product");

  const nameP = document.createElement("p");
  nameP.textContent = name;
  nameP.classList.add("name");

  const priceP = document.createElement("p");
  priceP.textContent = price.toString();
  priceP.classList.add("price");

  const descP = document.createElement("p");
  descP.textContent = description;
  descP.classList.add("description");

  div.append(nameP);
  div.append(descP);
  div.append(priceP);

  return div;
}

export async function populate(m: HTMLElement): Promise<void> {
  const data: Product[] = await getProducts();
  const children: HTMLParagraphElement[] = data.map(createProduct);

  m.replaceChildren(...children);
}

async function handleResponse(
  res: Response,
  populate: () => Promise<void>,
): Promise<void> {
  if (res.ok) {
    return populate();
  }
  throw new Error(JSON.stringify(await res.json(), undefined, 4));
}

export function setupPost(
  form: HTMLFormElement,
  populate: () => Promise<void>,
): void {
  function onSubmit(event: SubmitEvent): void {
    event.preventDefault();
    const data = new FormData(form);
    fetch(api, {
      method: "POST",
      body: data,
    })
      .then((res) => handleResponse(res, populate))
      .catch(console.error);
  }
  form.addEventListener("submit", onSubmit);
}
