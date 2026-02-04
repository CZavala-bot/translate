# Smartcontracts para TRANSLATE de Infoport

Esta carpeta contiene todo lo relativo al desarrollo, compilación, despliegue y verificación de los smartcontracts que se van a usar en el módulo de blockchain para el producto TRANSLATE de Infoport.

## Archivos y carpetas

Los siguientes elementos son relevantes:
- **hardhat.config.ts**: contiene los parámetro de conexión a la red, y el nombre de la red, está configurada 'quorumlocal' que es la red que se arranca desde /deployment/quorum-text-network'

 - **contracts**: carpeta que contiene los archivos .sol de los contratos. Se añade en este repo un contrato de ejemplo SimpleAssetContract.sol

 - **artifacts**: carpeta que se generará al compilar los contratos

 - **scripts**: carpeta con scripts de ejemplo para desplegar contrato, llamarlo para insertar y llamarlo para leer

## Comandos 

Desde una línea de comandos, que esté en esta carpeta, se pueden ejecutar distintos comandos:
 - compilar contratos
  `npx hardhat compile`

 - desplegar contrato, es decir, ejecutar el script que lo despliegua
 `npx hardhat run ./scripts/struct-string/deploy.ts --network quorum_infoport`
 IMPORTANTE: el despliegue de un contrato devuelve el `address` donde está desplegado en esa blockchain
             Para que los scripts de `insert.ts` o `read.ts`funcionen sobre él hay que 
             indicar el address en el archivo ./scripts/xxxxx/contract.json

 - insertar dato llamando al contrato
 `npx hardhat run ./scripts/struct-string/insert.ts --network quorum_infoport`

 - leer dato llamando al contrato
 `npx hardhat run ./scripts/struct-string/read.ts --network quorum_infoport`

 - verificar un contrato (cambiar el address por el obtenido en el despliegue) en el explorador de bloques de Blockscout
 `npx hardhat verify --network quorum_infoport 0xe135783649BfA7c9c4c6F8E528C7f56166efC8a6`

