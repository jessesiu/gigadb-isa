from isatools.model.v1 import *
from isatools.isatab import dumps
import xml.dom.minidom

def create_descriptor():
    dom = xml.dom.minidom.parse('/Users/xiaosizhe/Desktop/api100194.xml')
    root = dom.documentElement

    data = root.getElementsByTagName('dataset')
    dataset = data[0]

    print(dataset.nodeName)

    investigation = Investigation()
    investigation.studies.append(Study())


    # ------------ dataset ---------------

    investigation.studies[0].filename = "s_study.txt"
    investigation.studies[0].identifier = "10.5524/100001"
    investigation.studies[0].title = "test dataset"
    investigation.studies[0].description = "this is test dataset"
    investigation.studies[0].public_release_date = "2016/11/11"

    # submitter
    contact = Person(first_name="Alice", last_name="Robertson", affiliation="University of Life", email="tt@tt.com", roles=[OntologyAnnotation(term='submitter')])
    investigation.studies[0].contacts.append(contact)

    publication = Publication(doi="10.5524/manuscript10002")
    publication.status = OntologyAnnotation(term="published")
    investigation.studies[0].publications.append(publication)

    #Data Repository
    investigation.studies[0].comments = []
    comment1 = Comment(name="Data Repository", value="ftp://climb.genomics.cn")
    investigation.studies[0].comments.append(comment1)

    #Data Record Accession
    comment2 = Comment(name="Data Record Accession", value="ftp://climb.genomics.cn")
    investigation.studies[0].comments.append(comment2)

    ##funder
    comment3 = Comment(name="Funder Term Source REF", value="ftp://climb.genomics.cn") # funder url
    investigation.studies[0].comments.append(comment3)
    comment4 = Comment(name="Grant Identifier", value="National ....") # funder award
    investigation.studies[0].comments.append(comment4)
    comment5 = Comment(name="Awardee", value="National ....") # funder comment
    investigation.studies[0].comments.append(comment5)

    ##publication
    comment6 = Comment(name="Data Repository", value="GigaScience database") # publication
    investigation.studies[0].comments.append(comment6)

    ##author
    author1 = Person(first_name="Alice", last_name="Robertson", roles="author")
    #if contain orcid
    comment7 = Comment(name="Study Person ORCID", value="111111-22221-00000")
    investigation.studies[0].comments.append(comment7)

    ##dataset type eg. Genomics
    comment8 = Comment(name="Subject Keywords", value="Genomics")
    investigation.studies[0].comments.append(comment8)

    ##dataset keyword
    comment9 = Comment(name="key", value="rna sequences")
    investigation.studies[0].comments.append(comment9)

    # ------------ sample ---------------
    source = Source(name='source_material')
    investigation.studies[0].materials['sources'].append(source)
    prototype_sample = Sample(name='sample_material', derives_from=source)
    investigation.studies[0].materials['samples'] = batch_create_materials(prototype_sample, n=1)
    sample_collection_protocol = Protocol(name="sample collection",
                                          protocol_type=OntologyAnnotation(term="sample collection"))
    investigation.studies[0].protocols.append(sample_collection_protocol)

    sample_collection_process = Process(executes_protocol=sample_collection_protocol)
    investigation.studies[0].process_sequence.append(sample_collection_process);


    sample = Sample(name="SAMEA3518466") #sample name
    characteristic1 = Characteristic(category="Organism", value="Homo sapiens")
    sample.characteristics.append(characteristic1)
    characteristic2 = Characteristic(category="Term Source Ref", value="NCBITaxon")
    sample.characteristics.append(characteristic2)
    characteristic3 = Characteristic(category="Term Accession Number", value="http://")  #eol_link not need now
    sample.characteristics.append(characteristic3)

    # sample attribute

    characteristic4 = Characteristic(category="geolocation", value="10.222/2.00002222")  #eol_link not need now
    sample.characteristics.append(characteristic4)

    investigation.studies[0].materials['samples'].append(sample)


    for src in investigation.studies[0].materials['sources']:
        sample_collection_process.inputs.append(src)
    for sam in investigation.studies[0].materials['samples']:
        sample_collection_process.outputs.append(sam)


    # ------------ file ---------------

    assay = Assay(filename="a_assay.txt")

    datafile = DataFile(filename="ftp://xxxxxxxxx")
    datafile.comments = []
    comment10 = Comment(name="File Description", value="test file")
    datafile.comments.append(comment10)


    assay.data_files.append(datafile)

    investigation.studies[0].assays.append(assay)

    from isatools.isatab import dump
    return dump(isa_obj=investigation, output_path='/Users/xiaosizhe/Desktop')


if __name__ == '__main__':
    print(create_descriptor())


