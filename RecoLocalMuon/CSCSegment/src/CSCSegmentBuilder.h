#ifndef CSCSegment_CSCSegmentBuilder_h
#define CSCSegment_CSCSegmentBuilder_h

/** \class CSCSegmentBuilder 
 * Algorithm to build CSCSegment's from CSCRecHit2D collection
 * by implementing a 'build' function required by CSCSegmentProducer.
 *
 * Implementation notes: <BR>
 * Configured via the Producer's ParameterSet. <BR>
 * Presume this might become an abstract base class one day. <BR>
 *
 * \author M. Sani
 *
 *
 */

#include <DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h>
#include <DataFormats/CSCRecHit/interface/CSCWireHitCollection.h>
#include <DataFormats/CSCRecHit/interface/CSCStripHitCollection.h>
#include <DataFormats/CSCRecHit/interface/CSCSegmentCollection.h>
#include "CSCRecoConditions.h"

#include <FWCore/ParameterSet/interface/ParameterSet.h>

class CSCGeometry;
class CSCSegmentAlgorithm;
class CSCRecoConditions;

class CSCSegmentBuilder {
public:
   
    /** Configure the algorithm via ctor.
     * Receives ParameterSet percolated down from EDProducer
     * which owns this Builder.
     */
    explicit CSCSegmentBuilder(const edm::ParameterSet&);
    /// Destructor
    ~CSCSegmentBuilder();

    /** Find rechits in each CSCChamber, build CSCSegment's in each chamber,
     *  and fill into output collection.
     */
    void build(const CSCRecHit2DCollection* rechits,
               const CSCWireHitCollection* wirehits,
               const CSCStripHitCollection* striphits, CSCSegmentCollection& oc);

    /** Cache pointer to geometry _for current event_
     */
    void setGeometry(const CSCGeometry* geom);

    void setConditions ( CSCRecoConditions* reco );

private:

    const CSCGeometry* geom_;

    //    %::map<std::string, CSCSegmentAlgorithm*> algoMap;  //  forner
    std::map<std::string, std::unique_ptr<CSCSegmentAlgorithm>> algoMap;
    CSCRecoConditions* recoConditions_;

};

#endif
