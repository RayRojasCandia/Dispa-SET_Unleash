
DATAPACKAGE: CONVENTIONAL POWER PLANTS
===========================================================================

https://doi.org/10.25832/conventional_power_plants/2020-10-01

by Open Power System Data: http://www.open-power-system-data.org/

Package Version: 2020-10-01

List of conventional power plants in Germany and European countries

This datapackage contains data on conventional power plants for Germany as
well as other selected European countries. The data includes individual
power plants with their technical characteristics. These include installed
capacity, main energy source, type of technology, CHP capability, and
geographical information. The geographical scope is primarily on Germany
and its neighboring countries. The datapackage currently covers Germany,
Austria, Belgium, Switzerland, Czech Republic, Denmark, Spain, Finland,
France, Italy, the Netherlands, Norway, Poland, Sweden, Slovakia, Slovenia,
and United Kingdom. Due to varying data quality of publicly available data,
not all information can be provided for each country. Sources for European
countries comprise detailed power plants lists from national institutions,
ministries, or market participants as well as manually compiled lists of
power plants for countries without a system-wide power plant list. All data
processing is conducted in Python and pandas, and has been documented in
the Jupyter Notebooks linked below.

The data package covers the geographical region of Germany, Austria, Belgium, Switzerland, Czech Republic, Denmark, Spain, Finland, France, Italy, the Netherlands, Norway, Poland, Sweden, Slovakia, Slovenia, United Kingdom.

We follow the Data Package standard by the Frictionless Data project, a
part of the Open Knowledge Foundation: http://frictionlessdata.io/


Documentation and script
===========================================================================

This README only contains the most basic information about the data package.
For the full documentation, please see the notebook script that was used to
generate the data package. You can find it at:

https://nbviewer.jupyter.org/github/Open-Power-System-Data/conventional_power_plants/blob/2020-10-01/main.ipynb

Or on GitHub at:

https://github.com/Open-Power-System-Data/conventional_power_plants/blob/2020-10-01/main.ipynb

License and attribution
===========================================================================

Attribution:
    Attribution should be given as follows: Open Power System Data. 2020.
    Data Package Conventional power plants. Version 2020-10-01.
    https://doi.org/10.25832/conventional_power_plants/2020-10-01. (Primary
    data from various sources, for a complete list see URL).


Version history
===========================================================================

* 2020-10-01 Updated data to new powerplant lists, bugfixes
* 2018-12-20 Updated data to new powerplant lists, bugfixes
* 2018-02-27 Updated data to new powerplant lists
* 2017-07-07 Updated data and added EIC codes
* 2017-03-03 Updated data sources and spatial coverage by more European countries
* 2016-10-27 release


Resources
===========================================================================

* [Package description page](http://data.open-power-system-data.org/conventional_power_plants/2020-10-01/)
* [ZIP Package](http://data.open-power-system-data.org/conventional_power_plants/opsd-conventional_power_plants-2020-10-01.zip)
* [Script and documentation](https://github.com/Open-Power-System-Data/conventional_power_plants/blob/2020-10-01/main.ipynb)
* [Original input data](http://data.open-power-system-data.org/conventional_power_plants/2020-10-01/original_data/)


Sources
===========================================================================

* [BNetzA Kraftwerksliste (DE)](http://www.bundesnetzagentur.de/DE/Sachgebiete/ElektrizitaetundGas/Unternehmen_Institutionen/Versorgungssicherheit/Erzeugungskapazitaeten/Kraftwerksliste/kraftwerksliste-node.html)
* [Umweltbundesamt Datenbank Kraftwerke in Deutschland (DE)](http://www.umweltbundesamt.de/dokument/datenbank-kraftwerke-in-deutschland)
* [Verbund AG hydro power plants (AT)](https://www.verbund.com/en-at/about-verbund/power-plants/our-power-plants)
* Austria (AT) (several sources)
* [ELIA Generation facilities (BE)](http://www.elia.be/en/grid-data/power-generation/generating-facilities)
* [BFE Statistik der Wasserkraftanlagen der Schweiz (CH)](https://www.bfe.admin.ch/bfe/en/home/supply/renewable-energy/hydropower.html)
* [BFE Nuclear Energy (CH)](https://www.bfe.admin.ch/bfe/en/home/supply/statistics-and-geodata/geoinformation/geodata/nuclear-energy/nuclear-power-plants.html)
* [CEPS Available capacity (CZ)](https://www.ceps.cz/cs/priprava-provozu)
* Denmark (DK) (several sources)
* [SEDE Productores (ES)](https://sede.minetur.gob.es/en-US/datosabiertos/catalogo/registro-productores-electrica)
* [Energy authority Power plant register (FI)](https://energiavirasto.fi/toimitusvarmuus)
* [RTE List of production units with more than 100MW (FR)](https://www.services-rte.com/en/view-data-published-by-rte/production-installed-capacity.html)
* [TERNA Installed generation capacity (IT)](http://www.terna.it/it-it/sistemaelettrico/transparencyreport/generation/installedgenerationcapacity.aspx)
* [TenneT Available capacity (NL)](http://www.tennet.org/english/operational_management/export_data.aspx)
* [NVE Power Generation (NO)](https://www.nve.no/energiforsyning/kraftproduksjon/)
* [GPI List of generation units (PL)](http://gpi.tge.pl/en/wykaz-jednostek)
* Nordpool Power plant units (SE) (link inactive)
* Slovenia (SI) (several sources)
* [SEAS Power plants (SK)](https://www.seas.sk/thermal-power-plants)
* [Statistical office Power stations in the United Kingdom (Dukes 5.11) (UK)](https://www.gov.uk/government/statistics/electricity-chapter-5-digest-of-united-kingdom-energy-statistics-dukes)


Field documentation
===========================================================================

conventional_power_plants_DE.csv
---------------------------------------------------------------------------

* id
    - Type: string
    - Description: Power plant ID based on the ID provided in the BNetzA-list.
* name_bnetza
    - Type: string
    - Description: Power plant name as specified in the BNetzA power plant list
* block_bnetza
    - Type: string
    - Description: Block name as specified in the BNetzA power plant list
* name_uba
    - Type: string
    - Description: Power plant name according to UBA data
* company
    - Type: string
    - Description: Company name
* street
    - Type: string
    - Description: Street as specified in the BNetzA power plant list
* postcode
    - Type: string
    - Description: Postcode as specified in the BNetzA power plant list
* city
    - Type: string
    - Description: City as specified in the BNetzA power plant list
* state
    - Type: string
    - Description: State as specified in the BNetzA power plant list
* country
    - Type: string
    - Description: Two-letter ISO code
* capacity_net_bnetza
    - Type: number
    - Description: Net installed capacity based on BNetzA
* capacity_gross_uba
    - Type: number
    - Description: Gross installed capacity according to UBA data
* energy_source
    - Type: string
    - Description: Used fuel or energy source
* technology
    - Type: string
    - Description: Power plant technology or sort
* chp
    - Type: boolean
    - Description: Status of being able to supply heat
* chp_capacity_uba
    - Type: number
    - Description: Heat capacity according to UBA data
* commissioned
    - Type: integer
    - Description: Year of commissioning formatted as integer, using data from BNetzA and UBA
* commissioned_original
    - Type: string
    - Description: Year of commissioning (raw data)
* retrofit
    - Type: integer
    - Description: Year of modernization according to UBA data
* shutdown
    - Type: integer
    - Description: Year of decommissioning based on BNetzA data
* status
    - Type: string
    - Description: Power plant status
* type
    - Type: string
    - Description: Purpose of the produced power
* lat
    - Type: number
    - Description: Precise geographic coordinates - latitude
* lon
    - Type: number
    - Description: Precise geographic coordinates - longitude
* eic_code_plant
    - Type: string
    - Description: EIC code of plant
* eic_code_block
    - Type: string
    - Description: EIC code of block
* efficiency_data
    - Type: number
    - Description: Proportion between power output and input, self researched values
* efficiency_source
    - Type: string
    - Description: Source of efficiency data
* efficiency_estimate
    - Type: number
    - Description: Estimated proportion between power output and input
* energy_source_level_1
    - Type: string
    - Description: Energy source level 1 according to the documentation
* energy_source_level_2
    - Type: string
    - Description: Energy source level 2 according to the documentation
* energy_source_level_3
    - Type: string
    - Description: Energy source level 3 according to the documentation
* eeg
    - Type: boolean
    - Description: Status of being entitled to a renumeration
* network_node
    - Type: string
    - Description: Connection point to the electricity grid based on BNetzA data
* voltage
    - Type: string
    - Description: Grid or transformation level of the network node based on BNetzA data
* network_operator
    - Type: string
    - Description: Network operator of the grid or transformation level based on BNetzA data
* merge_comment
    - Type: string
    - Description: Comment on BNetzA - UBA merge
* comment
    - Type: string
    - Description: Further comments



conventional_power_plants_EU.csv
---------------------------------------------------------------------------

* name
    - Type: string
    - Description: Power plant name as specified in national data sources
* company
    - Type: string
    - Description: Company name
* street
    - Type: string
    - Description: Street as specified in national data source
* postcode
    - Type: string
    - Description: Postcode as specified in national data sourcee
* city
    - Type: string
    - Description: City as specified in national data source
* country
    - Type: string
    - Description: Two-letter ISO code
* capacity
    - Type: number
    - Description: Installed generation capacity in MW
* energy_source
    - Type: string
    - Description: Input energy source  (e.g., hard coal, lignite, nuclear)
* technology
    - Type: string
    - Description: Power plant technology (e.g., gas turbine, steam turbine)
* chp
    - Type: boolean
    - Description: Status of being able to supply heat
* commissioned
    - Type: number
    - Description: Year of commissioning formatted as integer, using data from BNetzA and UBA
* type
    - Type: string
    - Description: Purpose of the produced power (e.g. CHP or IPP)
* lat
    - Type: number
    - Description: Precise geographic coordinates - latitude
* lon
    - Type: number
    - Description: Precise geographic coordinates - longitude
* eic_code
    - Type: string
    - Description: EIC code
* energy_source_level_1
    - Type: string
    - Description: Energy source level 1 according to the documentation
* energy_source_level_2
    - Type: string
    - Description: Energy source level 2 according to the documentation
* energy_source_level_3
    - Type: string
    - Description: Energy source level 3 according to the documentation
* additional_info
    - Type: string
    - Description: Additional information on power plants as provided in national data source
* comment
    - Type: string
    - Description: Own OPSD comments on data entries (e.g., errors, missing data, inconsistencies)
* source
    - Type: string
    - Description: Source of information



Feedback
===========================================================================

Thank you for using data provided by Open Power System Data. If you have
any question or feedback, please do not hesitate to contact us.

For this data package, contact:
Jens Weibezahn <jew@wip.tu-berlin.de>

Richard Weinhold <riw@wip.tu-berlin.de>

Clemens Gerbaulet
Friedrich Kunz
For general issues, find our team contact details on our website:
http://www.open-power-system-data.org














